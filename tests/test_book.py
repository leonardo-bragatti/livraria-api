from http import HTTPStatus

import pytest

from livraria.auth.utils import verify_token
from main import app
from tests import client


def overrides_verify_token():
    pass


ENDPOINT = "/livros"
app.dependency_overrides[verify_token] = overrides_verify_token


@pytest.fixture
def book():
    return {
        "id": 1,
        "titulo": "Titulo",
        "isbn": "12345678901234",
        "paginas": 200,
        "ano": 2023,
        "capa": "http://site.com/imagem.jpg",
    }


@pytest.fixture
def books(book):
    return [book]


def test_create(book, mocker):
    mocker.patch("livraria.books.crud.create_book", return_value=book)
    response = client.post(
        ENDPOINT,
        json={
            "titulo": "Titulo",
            "isbn": "12345678901234",
            "paginas": 200,
            "ano": 2023,
            "capa": "http://site.com/imagem.jpg",
            "autorId": 1,
            "categoriaId": 1,
            "editoraId": 1,
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == book


def test_list(books, mocker):
    mocker.patch("livraria.books.crud.get_books", return_value=books)
    response = client.get(ENDPOINT)
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"items": books}


def test_not_found(book, mocker):
    mocker.patch("livraria.books.crud.get_book", return_value=None)
    response = client.get(f"{ENDPOINT}/1")
    assert response.status_code == HTTPStatus.NOT_FOUND


def test_get(book, mocker):
    mocker.patch("livraria.books.crud.get_book", return_value=book)
    response = client.get(f"{ENDPOINT}/1")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == book


def test_update(book, mocker):
    mocker.patch("livraria.books.crud.update_book", return_value=book)
    response = client.put(
        f"{ENDPOINT}/1",
        json={
            "titulo": "Titulo",
            "isbn": "12345678901234",
            "paginas": 321,
            "ano": 2023,
            "capa": "http://site.com/imagem.jpg",
            "autorId": 1,
            "categoriaId": 1,
            "editoraId": 1,
        },
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == book


def test_delete(book, mocker):
    mocker.patch("livraria.books.crud.delete_book", return_value=book)
    response = client.delete(f"{ENDPOINT}/1")
    assert response.status_code == HTTPStatus.OK
