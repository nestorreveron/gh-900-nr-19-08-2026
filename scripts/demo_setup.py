import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


def main() -> None:
    from scripts.generate_data import main as generate_data
    from scripts.init_db import reset_and_seed

    generate_data()
    reset_and_seed()
    print("Demo data and SQLite database are ready.")


if __name__ == "__main__":
    main()
