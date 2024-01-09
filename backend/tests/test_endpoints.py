import flask
from data_manager import DataManager, FilePaths
from utils import open_json
import pytest
from app import app


app.config.update(
    {
        "TESTING": True,
    }
)


@pytest.fixture
def client():
    return app.test_client()


@pytest.fixture
def filepaths():
    return FilePaths("./data/tasks.json")


@pytest.fixture
def tasks(filepaths):
    return open_json(filepaths.TASK_FILE, "r")


@pytest.fixture
def data_manager(filepaths):
    return DataManager(filepaths)


def test_get_tasks():
    with app.test_request_context("/api/v1/tasks/?user=Mia", method="GET"):
        assert flask.request.path == "/api/v1/tasks/"
        assert flask.request.method == "GET"
        assert flask.request.args.get("user") == "Mia"


def test_get_task(tasks):
    with app.test_request_context(f"/api/v1/tasks/{tasks[0]['slug']}", method="GET"):
        assert flask.request.path == f"/api/v1/tasks/{tasks[0]['slug']}"
        assert flask.request.method == "GET"


def test_get_home_page(client):
    response = client.get()
    assert response.status_code == 200, response.status_code
    assert b"Velkommen til Husansvars web api!" in response.data, response.data


def test_get_home_page_api(client):
    response = client.get("/api/v1")
    assert response.status_code == 200, response.status_code
    assert b"Velkommen til Husansvars web api!" in response.data, response.data


def test_get_tasks_return(client, data_manager):
    response = client.get("/api/v1/tasks/", query_string={"user": "Mia"})
    assert response.status_code == 200, response.data
    expected_content = str(data_manager.get_tasks_by_user("Mia")[0]["slug"]).encode()
    assert expected_content in response.data


def test_get_tasks_empty(client):
    response = client.get("/api/v1/tasks/", query_string={"user": "jibberish"})
    assert response.status_code == 404, response.status_code


def test_get_tasks_all(client):
    response = client.get("/api/v1/tasks/")
    assert response.status_code == 200, response.data
    assert b'"slug":' in response.data


def test_get_task_success(client, tasks):
    response = client.get(f"/api/v1/tasks/{tasks[0]['slug']}")
    assert response.status_code == 200
    assert b'"slug":' in response.data


def test_get_task_wrong(client):
    response = client.get("/api/v1/tasks/123")
    assert response.status_code == 404


def test_post_task(client):
    response = client.post("/api/v1/tasks/", json={"title": "test", "assignee": "test"})
    assert response.status_code == 200
    assert b'"slug":' in response.data


def test_delete_task(client, tasks):
    response = client.delete(f"/api/v1/tasks/{tasks[len(tasks)-1]['slug']}")
    assert response.status_code == 204


def test_edit_task(client, tasks):
    response = client.put(
        f"/api/v1/tasks/{tasks[0]['slug']}",
        json={"slug": tasks[0]["slug"], "title": "test", "assignee": "test"},
    )
    assert response.status_code == 200
