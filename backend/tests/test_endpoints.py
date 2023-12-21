import flask
from data_manager import DataManager
from utils import open_json
import pytest
from data_setup import TASK_FILE
from app import app


app.config.update(
    {
        "TESTING": True,
    }
)


# def app():
#     app = flask.current_app()

#     app.config.update(
#         {
#             "TESTING": True,
#         }
#     )
#     yield app


@pytest.fixture
def client():
    return app.test_client()


@pytest.fixture
def tasks():
    return open_json(TASK_FILE, "r")


@pytest.fixture
def data_manager(tasks):
    return DataManager(tasks)


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


def test_get_tasks_all(client, data_manager):
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
