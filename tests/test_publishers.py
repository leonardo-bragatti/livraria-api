from http import HTTPStatus

import pytest

from livraria.auth.utils import verify_token
from main import app
from tests import client


def overrides_verify_token():
    pass


ENDPOINT = "/editoras"
app.dependency_overrides[verify_token] = overrides_verify_token


@pytest.fixture
def publisher():
    return {"id": 1, "nome": "Editora Nome"}


@pytest.fixture
def publishers(publisher):
    return [publisher]


def test_create(publisher, mocker):
    mocker.patch("livraria.publishers.crud.create_publisher", return_value=publisher)
    response = client.post(
        ENDPOINT,
        json={"nome": "Publisher Test"},
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == publisher


def test_list(publishers, mocker):
    mocker.patch("livraria.publishers.crud.get_publishers", return_value=publishers)
    response = client.get(ENDPOINT)
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"items": publishers}


def test_not_found(mocker):
    mocker.patch("livraria.publishers.crud.get_publisher", return_value=None)
    response = client.get(f"{ENDPOINT}/1")
    assert response.status_code == HTTPStatus.NOT_FOUND


def test_get(publisher, mocker):
    mocker.patch("livraria.publishers.crud.get_publisher", return_value=publisher)
    response = client.get(f"{ENDPOINT}/1")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == publisher


def test_update(publisher, mocker):
    mocker.patch("livraria.publishers.crud.update_publisher", return_value=publisher)
    response = client.put(
        f"{ENDPOINT}/1",
        json={
            "nome": "Autor Test",
        },
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == publisher


def test_delete(publisher, mocker):
    mocker.patch("livraria.publishers.crud.delete_publisher", return_value=publisher)
    response = client.delete(f"{ENDPOINT}/1")
    assert response.status_code == HTTPStatus.OK
