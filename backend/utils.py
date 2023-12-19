import datetime
import json


def generate_slug(task_title: str) -> str:
    """Add task title and current time to create slug"""

    title = task_title.replace(" ", "_")
    timenow = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return title + "_" + timenow


def open_json(file_path: str, mode: str = "r", data=None):
    """Read and write to json file! If write, it returns the data"""
    if mode == "r":
        with open(file_path, mode, encoding="utf-8") as f:
            return json.load(f)

    elif mode == "w" and data is not None:
        with open(file_path, mode, encoding="utf-8") as f:
            json.dump(data, f)
    else:
        raise ValueError("Invalid mode")
