import flask
from data_setup import (
    ensure_data_setup,
    wipe_existing_data,
    generate_test_tasks,
    TASK_FILE,
)
from utils import open_json
from data_manager import DataManager
from logger import setup_logger

# wipe_existing_data()  # only run when developing
status = ensure_data_setup()
if status:
    generate_test_tasks()
app = flask.Flask(__name__)

log = setup_logger()


@app.route("/")
def info():
    # add template...
    return "<h1>Velkommen til Husansvars web api!</h1>"


@app.route("/api/v1")
def infoApi():
    # show availalbe endpoints
    # add template...
    return "<h1>Velkommen til Husansvars web api!</h1>"


@app.get("/api/v1/tasks/")
def getTasks():
    user = flask.request.args.get("user")
    tasks: list = open_json(TASK_FILE, "r")
    dataManager = DataManager(tasks)
    return dataManager.get_tasks_by_user(user)


@app.get("/api/v1/tasks/<slug>")
def getTask(slug):
    """Return a single task element or 404 if not found"""
    tasks: list = open_json(TASK_FILE, "r")
    slug_task = DataManager(tasks).get_task_by_slug(slug)
    if slug_task is None:
        flask.abort(404, description="Task with slug not found")
    return slug_task


with app.test_request_context():
    print(flask.url_for("getTask", slug="Vask_bad_2023-12-20_22:42:10"))
