import flask

# add --host=0.0.0.0 to make visible externally...

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

@app.route("/api/v1/mia/tasks")
def getMiasTasks():
    return [{
        "id": 1,
    },
    {
        "id": 2,
    }]


@app.route("/api/v1/mia/tasks/<int:id>")
def getMiaTask(id):
    return {
        "id": id,
    }


@app.errorhandler(404)
def handleError():
    # add template...
    return "Wrong url, page not found";
