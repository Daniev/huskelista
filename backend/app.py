import flask
import json
from data_manager import DataManager, FilePaths
from logger import setup_logger

app = flask.Flask(__name__)
fp = FilePaths("./data/tasks.json")
dm = DataManager(fp)

# dm.wipe_existing_data()  # only run when developing
status = dm.ensure_data_setup()
# dm.generate_test_tasks()

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
    user_tasks = dm.get_tasks_by_user(user)
    if len(user_tasks) == 0:
        flask.abort(
            404,
            description="No tasks found in database for the provided user, you should create some",
        )
    return user_tasks


@app.post("/api/v1/tasks/")
def create_task():
    """Create a new task element"""
    task = json.loads(flask.request.data)
    dm.add_task_to_file(task)
    return task


@app.delete("/api/v1/tasks/<slug>")
def delete_task(slug):
    """Handle the delete request for a single task element"""
    dm.delete_task(slug)
    return "", 204


@app.get("/api/v1/tasks/<slug>")
def getTask(slug):
    """Return a single task element or 404 if not found"""
    slug_task = dm.get_task_by_slug(slug)
    if slug_task is None:
        flask.abort(404, description="Task with slug not found")
    return slug_task


with app.test_request_context():
    print(flask.url_for("getTask", slug="Vask_bad_2023-12-20_22:42:10"))
