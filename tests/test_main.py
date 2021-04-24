import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_get_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"mensaje": "hola mundo"}


@pytest.mark.parametrize("input,expected", [(1, 1), (2, 2), (3, 3)])
def test_get_item_id(input, expected):
    response = client.get(f"/items/{input}")
    assert response.status_code == 200
    assert response.json() == {"item_id": expected}
