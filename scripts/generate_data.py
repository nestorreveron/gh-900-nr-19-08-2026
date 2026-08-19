import csv
import random
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
RANDOM = random.Random(900)

COMPANIES = [
    "Contoso", "Fabrikam", "Northwind Traders", "Adventure Works", "Tailspin Toys",
    "Woodgrove Bank", "Alpine Ski House", "Wide World Importers", "Litware", "Proseware",
    "Trey Research", "Fourth Coffee",
]
COUNTRIES = ["España", "México", "Chile", "Colombia", "Perú", "Canadá", "Portugal", "Argentina"]
INDUSTRIES = ["Tecnología", "Finanzas", "Retail", "Educación", "Salud", "Manufactura"]
PRODUCTS = [
    "Contoso CRM", "Contoso Analytics", "Contoso ERP", "Contoso SecureMail",
    "Contoso AI Assistant", "Contoso Cloud Backup", "Contoso Collaboration Hub",
    "Contoso Identity Manager", "Contoso Security Center", "Contoso Data Platform",
]


def write_csv(filename: str, rows: list[dict[str, object]]) -> None:
    DATA_DIR.mkdir(exist_ok=True)
    with (DATA_DIR / filename).open("w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def customers() -> list[dict[str, object]]:
    rows = []
    for index in range(1, 201):
        company = RANDOM.choice(COMPANIES)
        country = RANDOM.choice(COUNTRIES)
        rows.append({
            "id": index,
            "name": f"{company} Demo Customer {index:03d}",
            "email": f"customer{index:03d}@contoso.example",
            "phone": f"+1-555-010-{index % 10000:04d}",
            "country": country,
            "industry": RANDOM.choice(INDUSTRIES),
            "address": f"{index} Training Avenue, {country}",
            "created_at": (date(2025, 1, 1) + timedelta(days=index % 365)).isoformat(),
        })
    return rows


def products() -> list[dict[str, object]]:
    rows = []
    categories = ["SaaS", "Security", "Data", "Productivity", "AI"]
    for index in range(1, 51):
        product = PRODUCTS[(index - 1) % len(PRODUCTS)]
        rows.append({
            "id": index,
            "name": f"{product} {index:02d}",
            "category": RANDOM.choice(categories),
            "price": f"{RANDOM.randint(20, 900) + .99:.2f}",
            "status": RANDOM.choice(["active", "preview", "retired"]),
            "description": f"Producto ficticio {product} para laboratorios GH-900.",
        })
    return rows


def orders(customer_count: int = 200, product_count: int = 50) -> list[dict[str, object]]:
    rows = []
    for index in range(1, 501):
        quantity = RANDOM.randint(1, 8)
        price = RANDOM.randint(30, 1000) + .99
        rows.append({
            "id": index,
            "customer_id": RANDOM.randint(1, customer_count),
            "product_id": RANDOM.randint(1, product_count),
            "quantity": quantity,
            "order_date": (date(2025, 6, 1) + timedelta(days=index % 365)).isoformat(),
            "status": RANDOM.choice(["pending", "processing", "completed", "cancelled"]),
            "total": f"{quantity * price:.2f}",
        })
    return rows


def tickets(customer_count: int = 200) -> list[dict[str, object]]:
    subjects = ["Login assistance", "Billing question", "Product setup", "Performance review"]
    rows = []
    for index in range(1, 101):
        rows.append({
            "id": index,
            "customer_id": RANDOM.randint(1, customer_count),
            "subject": f"{RANDOM.choice(subjects)} #{index:03d}",
            "description": "Ticket ficticio para demostrar Issues, soporte y revisiones.",
            "priority": RANDOM.choice(["low", "medium", "high", "critical"]),
            "status": RANDOM.choice(["open", "in_progress", "resolved", "closed"]),
            "created_at": f"2026-01-{(index % 28) + 1:02d}T09:00:00",
        })
    return rows


def main() -> None:
    write_csv("customers.csv", customers())
    write_csv("products.csv", products())
    write_csv("orders.csv", orders())
    write_csv("support_tickets.csv", tickets())


if __name__ == "__main__":
    main()
