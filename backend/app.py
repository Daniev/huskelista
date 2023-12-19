import flask
from data_setup import ensure_data_setup, wipe_existing_data, generate_test_tasks

wipe_existing_data()  # only run when developing
ensure_data_setup()
generate_test_tasks()
app = flask.Flask(__name__)


@app.route("/")
def info():
    # add template...
    return "<h1>Velkommen til Husansvars web api!</h1>"


@app.route("/api/v1")
def infoApi():
    # show availalbe endpoints
    # add template...
    return "<h1>Velkommen til Husansvars web api!</h1>"


@app.route("/api/v1/tasks/<string:user>")
def getMiasTasks(user):
    return [
        {
            "id": 1,
        },
        {
            "id": 2,
        },
    ]


@app.route("/api/v1/tasks/<string:slug><string:user>")
def getMiaTask(slug, user):
    # lookup task by id or slug,
    # check if the user is the correct user
    return {
        "id": id,
    }
