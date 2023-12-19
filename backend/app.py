import flask
import datetime

# add --host=0.0.0.0 to make visible externally...

app = flask.Flask(__name__)


def generate_slug(task_title: str) -> str:
    """Add task title and current time to create slug"""
    timenow = str(datetime.datetime.now())
    return task_title + "_" + timenow


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
