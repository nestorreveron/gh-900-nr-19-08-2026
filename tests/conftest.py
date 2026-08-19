import pytest

from app import create_app
from app.config import Config
from scripts.init_db import reset_and_seed


@pytest.fixture()
def client(tmp_path):
    database_url = f"sqlite:///{tmp_path / 'contoso-test.db'}"

    class TestConfig(Config):
        DATABASE_URL = database_url
        TESTING = True

    app = create_app(TestConfig)
    reset_and_seed(database_url)
    with app.test_client() as test_client:
        yield test_client
