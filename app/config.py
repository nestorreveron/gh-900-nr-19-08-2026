import os
from pathlib import Path


class Config:
    BASE_DIR = Path(__file__).resolve().parent.parent
    INSTANCE_DIR = BASE_DIR / "instance"
    INSTANCE_DIR.mkdir(exist_ok=True)
    DATABASE_URL = os.getenv("DATABASE_URL", f"sqlite:///{INSTANCE_DIR / 'contoso.db'}")
    JSON_SORT_KEYS = False
