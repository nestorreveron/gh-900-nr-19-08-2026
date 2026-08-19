import csv
import sys
from datetime import date, datetime
from decimal import Decimal
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

DATA_DIR = ROOT / "data"


def load_csv(filename: str) -> list[dict[str, str]]:
    with (DATA_DIR / filename).open(encoding="utf-8") as csv_file:
        return list(csv.DictReader(csv_file))


def reset_and_seed(database_url: str | None = None) -> None:
    from app.config import Config
    from app.database import get_session, init_database
    from app.models import Customer, Order, Product, SupportTicket

    init_database(database_url or Config.DATABASE_URL)
    with get_session() as session:
        session.query(SupportTicket).delete()
        session.query(Order).delete()
        session.query(Product).delete()
        session.query(Customer).delete()
        for row in load_csv("customers.csv"):
            session.add(
                Customer(
                    id=int(row["id"]),
                    name=row["name"],
                    email=row["email"],
                    phone=row["phone"],
                    country=row["country"],
                    industry=row["industry"],
                    address=row["address"],
                    created_at=date.fromisoformat(row["created_at"]),
                )
            )
        for row in load_csv("products.csv"):
            session.add(
                Product(
                    id=int(row["id"]),
                    name=row["name"],
                    category=row["category"],
                    price=Decimal(row["price"]),
                    status=row["status"],
                    description=row["description"],
                )
            )
        for row in load_csv("orders.csv"):
            session.add(
                Order(
                    id=int(row["id"]),
                    customer_id=int(row["customer_id"]),
                    product_id=int(row["product_id"]),
                    quantity=int(row["quantity"]),
                    order_date=date.fromisoformat(row["order_date"]),
                    status=row["status"],
                    total=Decimal(row["total"]),
                )
            )
        for row in load_csv("support_tickets.csv"):
            session.add(
                SupportTicket(
                    id=int(row["id"]),
                    customer_id=int(row["customer_id"]),
                    subject=row["subject"],
                    description=row["description"],
                    priority=row["priority"],
                    status=row["status"],
                    created_at=datetime.fromisoformat(row["created_at"]),
                )
            )


if __name__ == "__main__":
    reset_and_seed()
    print("Database initialized with fictitious Contoso training data.")
