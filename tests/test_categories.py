from http import HTTPStatus

import pytest

from livraria.auth.utils import verify_token
from main import app
from tests import client


def overrides_verify_token():
    pass


ENDPOINT = "/categorias"
app.dependency_overrides[verify_token] = overrides_verify_token


@pytest.fixture
def category():
    return {"id": 1, "nome": "Categoria Nome"}


@pytest.fixture
def categories(category):
    return [category]


def test_create(category, mocker):
    create_category = mocker.patch("livraria.categories.crud.create_category")
    create_category.return_value = category
    response = client.post(
        ENDPOINT,
        json={"nome": "category Test"},
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == category


def test_list(categories, mocker):
    get_categories = mocker.patch("livraria.categories.crud.get_categories")
    get_categories.return_value = categories
    response = client.get(ENDPOINT)
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"items": categories}


def test_not_found(category, mocker):
    get_category = mocker.patch("livraria.categories.crud.get_category")
    get_category.return_value = None
    response = client.get(f"{ENDPOINT}/1")
    assert response.status_code == HTTPStatus.NOT_FOUND


def test_get(category, mocker):
    get_category = mocker.patch("livraria.categories.crud.get_category")
    get_category.return_value = category
    response = client.get(f"{ENDPOINT}/1")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == category


def test_update(category, mocker):
    update_category = mocker.patch("livraria.categories.crud.update_category")
    update_category.return_value = category
    response = client.put(
        f"{ENDPOINT}/1",
        json={
            "nome": "Autor Test",
        },
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == category


def test_delete(mocker):
    mocker.patch("livraria.categories.crud.delete_category")
    response = client.delete(f"{ENDPOINT}/1")
    assert response.status_code == HTTPStatus.OK
