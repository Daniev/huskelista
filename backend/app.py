import flask
import json
from data_setup import (
    ensure_data_setup,
    wipe_existing_data,
    generate_test_tasks,
    TASK_FILE,
)
from utils import open_json
from data_manager import DataManager
from logger import setup_logger

# various configuration and resetting of data
wipe = False
if wipe:
    wipe_existing_data()  # only run when developing

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
    """Return all tasks beloing to the user, or all if no user is provided. Return 404 if no data is found"""
    user = flask.request.args.get("user")
    tasks: list = open_json(TASK_FILE, "r")
    if len(tasks) == 0:
        flask.abort(
            404, description="No tasks found in database, you should create some"
        )
    if user is None:
        return tasks
    user_tasks = DataManager(tasks).get_tasks_by_user(user)
    if len(user_tasks) == 0:
        flask.abort(404, description="No tasks found for user")
    return user_tasks


@app.post("/api/v1/tasks/")
def create_task():
    """Create a new task element"""
    task = json.loads(flask.request.data)
    dm = DataManager()
    dm.add_task_to_file(task)
    return task


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
