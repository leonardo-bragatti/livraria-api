from http import HTTPStatus

import pytest

from livraria.auth.utils import verify_token
from main import app
from tests import client


def overrides_verify_token():
    pass


ENDPOINT = "/autores"
app.dependency_overrides[verify_token] = overrides_verify_token


@pytest.fixture
def author():
    return {"id": 1, "nome": "Autor Nome"}


@pytest.fixture
def authors(author):
    return [author]


def test_create(author, mocker):
    mocker.patch("livraria.authors.crud.create_author", return_value=author)
    response = client.post(
        ENDPOINT,
        json={"nome": "Author Test"},
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == author


def test_list(authors, mocker):
    mocker.patch("livraria.authors.crud.get_authors", return_value=authors)
    response = client.get(ENDPOINT)
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"items": authors}


def test_not_found(author, mocker):
    mocker.patch("livraria.authors.crud.get_author", return_value=None)
    response = client.get(f"{ENDPOINT}/1")
    assert response.status_code == HTTPStatus.NOT_FOUND


def test_get(author, mocker):
    mocker.patch("livraria.authors.crud.get_author", return_value=author)
    response = client.get(f"{ENDPOINT}/1")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == author


def test_update(author, mocker):
    mocker.patch("livraria.authors.crud.update_author", return_value=author)
    response = client.put(
        f"{ENDPOINT}/1",
        json={
            "nome": "Autor Test",
        },
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == author


def test_delete(author, mocker):
    mocker.patch("livraria.authors.crud.delete_author", return_value=author)
    response = client.delete(f"{ENDPOINT}/1")
    assert response.status_code == HTTPStatus.OK
