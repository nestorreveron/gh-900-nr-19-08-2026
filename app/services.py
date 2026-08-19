from datetime import UTC, date, datetime
from decimal import Decimal
from typing import Any

from sqlalchemy import func, or_, select
from sqlalchemy.orm import Session, joinedload

from app.models import Customer, Order, Product, SupportTicket

VALID_ORDER_STATUSES = {"pending", "processing", "completed", "cancelled"}
VALID_TICKET_STATUSES = {"open", "in_progress", "resolved", "closed"}
VALID_PRIORITIES = {"low", "medium", "high", "critical"}


def response(
    data: Any = None, message: str = "ok", errors: list[str] | None = None
) -> dict[str, Any]:
    return {"success": errors is None, "message": message, "data": data, "errors": errors or []}


def customer_to_dict(customer: Customer) -> dict[str, Any]:
    return {
        "id": customer.id,
        "name": customer.name,
        "email": customer.email,
        "phone": customer.phone,
        "country": customer.country,
        "industry": customer.industry,
        "address": customer.address,
        "created_at": customer.created_at.isoformat(),
    }


def product_to_dict(product: Product) -> dict[str, Any]:
    return {
        "id": product.id,
        "name": product.name,
        "category": product.category,
        "price": float(product.price),
        "status": product.status,
        "description": product.description,
    }


def order_to_dict(order: Order) -> dict[str, Any]:
    return {
        "id": order.id,
        "customer_id": order.customer_id,
        "customer_name": order.customer.name if order.customer else None,
        "product_id": order.product_id,
        "product_name": order.product.name if order.product else None,
        "quantity": order.quantity,
        "order_date": order.order_date.isoformat(),
        "status": order.status,
        "total": float(order.total),
    }


def ticket_to_dict(ticket: SupportTicket) -> dict[str, Any]:
    return {
        "id": ticket.id,
        "customer_id": ticket.customer_id,
        "customer_name": ticket.customer.name if ticket.customer else None,
        "subject": ticket.subject,
        "description": ticket.description,
        "priority": ticket.priority,
        "status": ticket.status,
        "created_at": ticket.created_at.isoformat(),
    }


def list_customers(session: Session) -> list[dict[str, Any]]:
    customers = session.scalars(select(Customer).order_by(Customer.id)).all()
    return [customer_to_dict(customer) for customer in customers]


def get_customer(session: Session, customer_id: int) -> dict[str, Any] | None:
    customer = session.get(Customer, customer_id)
    return customer_to_dict(customer) if customer else None


def search_customers(session: Session, query: str) -> list[dict[str, Any]]:
    normalized = f"%{query.strip().lower()}%"
    # TODO: Educational improvement opportunity: replace this broad search with indexed filters.
    customers = session.scalars(
        select(Customer)
        .where(
            or_(
                func.lower(Customer.name).like(normalized),
                func.lower(Customer.country).like(normalized),
                func.lower(Customer.industry).like(normalized),
                func.lower(Customer.email).like(normalized),
            )
        )
        .order_by(Customer.id)
    ).all()
    return [customer_to_dict(customer) for customer in customers]


def create_customer(
    session: Session, payload: dict[str, Any]
) -> tuple[dict[str, Any] | None, list[str]]:
    required = ["name", "email", "phone", "country", "industry", "address"]
    errors = _missing_fields(payload, required)
    email = str(payload.get("email", "")).strip().lower()
    if email and "@" not in email:
        errors.append("email must contain @")
    if errors:
        return None, errors
    customer = Customer(
        name=str(payload["name"]).strip(),
        email=email,
        phone=str(payload["phone"]).strip(),
        country=str(payload["country"]).strip(),
        industry=str(payload["industry"]).strip(),
        address=str(payload["address"]).strip(),
        created_at=date.today(),
    )
    session.add(customer)
    session.flush()
    return customer_to_dict(customer), []


def list_products(session: Session) -> list[dict[str, Any]]:
    products = session.scalars(select(Product).order_by(Product.id)).all()
    return [product_to_dict(product) for product in products]


def get_product(session: Session, product_id: int) -> dict[str, Any] | None:
    product = session.get(Product, product_id)
    return product_to_dict(product) if product else None


def list_orders(session: Session) -> list[dict[str, Any]]:
    orders = session.scalars(
        select(Order)
        .options(joinedload(Order.customer), joinedload(Order.product))
        .order_by(Order.id)
    ).all()
    return [order_to_dict(order) for order in orders]


def get_order(session: Session, order_id: int) -> dict[str, Any] | None:
    order = session.scalars(
        select(Order)
        .options(joinedload(Order.customer), joinedload(Order.product))
        .where(Order.id == order_id)
    ).first()
    return order_to_dict(order) if order else None


def create_order(
    session: Session, payload: dict[str, Any]
) -> tuple[dict[str, Any] | None, list[str]]:
    errors = _missing_fields(payload, ["customer_id", "product_id", "quantity"])
    customer_id = _positive_int(payload.get("customer_id"), "customer_id", errors)
    product_id = _positive_int(payload.get("product_id"), "product_id", errors)
    quantity = _positive_int(payload.get("quantity"), "quantity", errors)
    status = str(payload.get("status", "pending")).lower()
    if status not in VALID_ORDER_STATUSES:
        errors.append("status is not valid")
    customer = session.get(Customer, customer_id) if customer_id else None
    product = session.get(Product, product_id) if product_id else None
    if customer_id and not customer:
        errors.append("customer_id was not found")
    if product_id and not product:
        errors.append("product_id was not found")
    if errors or not product:
        return None, errors
    order = Order(
        customer_id=customer_id,
        product_id=product_id,
        quantity=quantity,
        order_date=date.today(),
        status=status,
        total=Decimal(quantity) * product.price,
    )
    session.add(order)
    session.flush()
    order.customer = customer
    order.product = product
    return order_to_dict(order), []


def list_tickets(session: Session) -> list[dict[str, Any]]:
    tickets = session.scalars(
        select(SupportTicket).options(joinedload(SupportTicket.customer)).order_by(SupportTicket.id)
    ).all()
    return [ticket_to_dict(ticket) for ticket in tickets]


def get_ticket(session: Session, ticket_id: int) -> dict[str, Any] | None:
    ticket = session.scalars(
        select(SupportTicket)
        .options(joinedload(SupportTicket.customer))
        .where(SupportTicket.id == ticket_id)
    ).first()
    return ticket_to_dict(ticket) if ticket else None


def create_ticket(
    session: Session, payload: dict[str, Any]
) -> tuple[dict[str, Any] | None, list[str]]:
    errors = _missing_fields(payload, ["customer_id", "subject", "description"])
    customer_id = _positive_int(payload.get("customer_id"), "customer_id", errors)
    priority = str(payload.get("priority", "medium")).lower()
    if priority not in VALID_PRIORITIES:
        errors.append("priority is not valid")
    customer = session.get(Customer, customer_id) if customer_id else None
    if customer_id and not customer:
        errors.append("customer_id was not found")
    if errors:
        return None, errors
    ticket = SupportTicket(
        customer_id=customer_id,
        subject=str(payload["subject"]).strip(),
        description=str(payload["description"]).strip(),
        priority=priority,
        status="open",
        created_at=datetime.now(UTC).replace(tzinfo=None),
    )
    session.add(ticket)
    session.flush()
    ticket.customer = customer
    return ticket_to_dict(ticket), []


def update_ticket_status(
    session: Session, ticket_id: int, payload: dict[str, Any]
) -> tuple[dict[str, Any] | None, list[str]]:
    status = str(payload.get("status", "")).lower()
    if status not in VALID_TICKET_STATUSES:
        return None, ["status is not valid"]
    ticket = session.scalars(
        select(SupportTicket)
        .options(joinedload(SupportTicket.customer))
        .where(SupportTicket.id == ticket_id)
    ).first()
    if ticket is None:
        return None, ["ticket was not found"]
    ticket.status = status
    session.flush()
    return ticket_to_dict(ticket), []


def dashboard(session: Session) -> dict[str, Any]:
    total_revenue = session.scalar(select(func.coalesce(func.sum(Order.total), 0))) or 0
    return {
        "customers": session.scalar(select(func.count(Customer.id))),
        "products": session.scalar(select(func.count(Product.id))),
        "orders": session.scalar(select(func.count(Order.id))),
        "open_tickets": session.scalar(
            select(func.count(SupportTicket.id)).where(
                SupportTicket.status.in_(["open", "in_progress"])
            )
        ),
        "revenue": float(total_revenue),
    }


def _missing_fields(payload: dict[str, Any], required: list[str]) -> list[str]:
    return [f"{field} is required" for field in required if not str(payload.get(field, "")).strip()]


def _positive_int(value: Any, field: str, errors: list[str]) -> int | None:
    try:
        parsed = int(value)
    except (TypeError, ValueError):
        errors.append(f"{field} must be a positive integer")
        return None
    if parsed <= 0:
        errors.append(f"{field} must be a positive integer")
        return None
    return parsed
