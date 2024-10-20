from fastapi.testclient import TestClient

from livraria.database import get_db
from main import app


def overrides_get_db():
    pass


app.dependency_overrides[get_db] = overrides_get_db
client = TestClient(app)
