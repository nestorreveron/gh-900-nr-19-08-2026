
import pytest

from app import create_app
from app.config import Config
from scripts.generate_data import main as generate_data
from scripts.init_db import reset_and_seed


class TestConfig(Config):
    DATABASE_URL = "sqlite:///:memory:"
    TESTING = True


@pytest.fixture()
def client():
    generate_data()
    app = create_app(TestConfig)
    reset_and_seed(TestConfig.DATABASE_URL)
    with app.test_client() as test_client:
        yield test_client
