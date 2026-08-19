from collections.abc import Callable
from typing import Any

from flask import Blueprint, jsonify, render_template, request
from sqlalchemy.exc import IntegrityError

from app import services
from app.database import get_session

bp = Blueprint("main", __name__)


def json_result(
    data: Any = None, status: int = 200, message: str = "ok", errors: list[str] | None = None
):
    return jsonify(services.response(data=data, message=message, errors=errors)), status


def not_found(resource: str):
    return json_result(
        status=404, message=f"{resource} not found", errors=[f"{resource} not found"]
    )


def with_session(handler: Callable[..., Any]):
    try:
        with get_session() as session:
            return handler(session)
    except IntegrityError:
        return json_result(status=409, message="duplicate record", errors=["record already exists"])
    except ValueError as exc:
        return json_result(status=400, message="invalid request", errors=[str(exc)])


@bp.get("/")
def index():
    return render_template("index.html")


@bp.get("/customers")
def customers_page():
    return render_template("customers.html")


@bp.get("/products")
def products_page():
    return render_template("products.html")


@bp.get("/orders")
def orders_page():
    return render_template("orders.html")


@bp.get("/support")
def support_page():
    return render_template("support.html")


@bp.get("/dashboard")
def dashboard_page():
    return render_template("dashboard.html")


@bp.get("/health")
def health():
    return json_result({"status": "healthy", "service": "contoso-customer-portal"})


@bp.get("/api/customers")
def api_customers():
    return with_session(lambda session: json_result(services.list_customers(session)))


@bp.get("/api/customers/search")
def api_customer_search():
    query = request.args.get("q", "").strip()
    if len(query) < 2:
        return json_result(
            status=400, message="invalid query", errors=["q must have at least 2 characters"]
        )
    return with_session(lambda session: json_result(services.search_customers(session, query)))


@bp.get("/api/customers/<int:customer_id>")
def api_customer(customer_id: int):
    def handler(session):
        customer = services.get_customer(session, customer_id)
        return json_result(customer) if customer else not_found("customer")

    return with_session(handler)


@bp.post("/api/customers")
def api_create_customer():
    payload = request.get_json(silent=True) or {}

    def handler(session):
        customer, errors = services.create_customer(session, payload)
        if errors:
            return json_result(status=400, errors=errors)
        return json_result(customer, 201, "created")

    return with_session(handler)


@bp.get("/api/products")
def api_products():
    return with_session(lambda session: json_result(services.list_products(session)))


@bp.get("/api/products/<int:product_id>")
def api_product(product_id: int):
    def handler(session):
        product = services.get_product(session, product_id)
        return json_result(product) if product else not_found("product")

    return with_session(handler)


@bp.get("/api/orders")
def api_orders():
    return with_session(lambda session: json_result(services.list_orders(session)))


@bp.get("/api/orders/<int:order_id>")
def api_order(order_id: int):
    def handler(session):
        order = services.get_order(session, order_id)
        return json_result(order) if order else not_found("order")

    return with_session(handler)


@bp.post("/api/orders")
def api_create_order():
    payload = request.get_json(silent=True) or {}

    def handler(session):
        order, errors = services.create_order(session, payload)
        if errors:
            return json_result(status=400, errors=errors)
        return json_result(order, 201, "created")

    return with_session(handler)


@bp.get("/api/support")
def api_support():
    return with_session(lambda session: json_result(services.list_tickets(session)))


@bp.get("/api/support/<int:ticket_id>")
def api_ticket(ticket_id: int):
    def handler(session):
        ticket = services.get_ticket(session, ticket_id)
        return json_result(ticket) if ticket else not_found("ticket")

    return with_session(handler)


@bp.post("/api/support")
def api_create_ticket():
    payload = request.get_json(silent=True) or {}

    def handler(session):
        ticket, errors = services.create_ticket(session, payload)
        if errors:
            return json_result(status=400, errors=errors)
        return json_result(ticket, 201, "created")

    return with_session(handler)


@bp.patch("/api/support/<int:ticket_id>")
def api_update_ticket(ticket_id: int):
    payload = request.get_json(silent=True) or {}

    def handler(session):
        ticket, errors = services.update_ticket_status(session, ticket_id, payload)
        if errors and errors == ["ticket was not found"]:
            return not_found("ticket")
        return json_result(ticket) if not errors else json_result(status=400, errors=errors)

    return with_session(handler)


@bp.get("/api/dashboard")
def api_dashboard():
    return with_session(lambda session: json_result(services.dashboard(session)))
