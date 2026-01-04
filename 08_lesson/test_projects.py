import uuid
import pytest
from client import YougileClient


def unique_name(prefix: str) -> str:
    return f"{prefix}_{uuid.uuid4()}"


@pytest.fixture
def api():
    return YougileClient()


@pytest.fixture
def created_project_id(api: YougileClient) -> str:
    payload = {"title": unique_name("project")}
    resp = api.create_project(payload)

    assert resp.status_code in (200, 201), resp.text
    project_id = resp.json().get("id") or resp.json().get("_id")
    assert project_id is not None

    return str(project_id)


def test_post_project_positive(api: YougileClient):
    payload = {"title": unique_name("positive")}
    resp = api.create_project(payload)

    assert resp.status_code in (200, 201), resp.text
    assert resp.json() is not None


def test_post_project_negative_empty_body(api: YougileClient):
    resp = api.create_project({})

    assert resp.status_code in (400, 422), resp.text


def test_get_project_positive(api: YougileClient, created_project_id: str):
    resp = api.get_project(created_project_id)

    assert resp.status_code == 200, resp.text
    assert resp.json().get("id") or resp.json().get("_id")


def test_get_project_negative_not_found(api: YougileClient):
    resp = api.get_project("000000000000000000000000")

    assert resp.status_code in (400, 404), resp.text


def test_put_project_positive(api: YougileClient, created_project_id: str):
    new_title = unique_name("updated")
    resp = api.update_project(created_project_id, {"title": new_title})

    assert resp.status_code in (200, 204), resp.text

    check = api.get_project(created_project_id)
    assert check.status_code == 200
    assert check.json().get("title") == new_title


def test_put_project_negative_invalid_id(api: YougileClient):
    resp = api.update_project("not-an-id", {"title": unique_name("x")})

    assert resp.status_code in (400, 404), resp.text
