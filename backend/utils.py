import datetime
import json
from logger import setup_logger


log = setup_logger()


def generate_slug(task_title: str) -> str:
    """Add task title and current time to create slug"""

    if task_title is None or task_title == "":
        return None
    title = task_title.replace(" ", "_")
    timenow = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return title + "_" + timenow.replace(" ", "_")


def open_json(file_path: str, mode: str = "r", data=None):
    """Read and write to json file! If write, it returns the data"""
    if mode == "r":
        try:
            with open(file_path, mode, encoding="utf-8") as f:
                return json.load(f)
        except json.decoder.JSONDecodeError:
            log.warn("Failed to read json file...")
            return None

    elif mode == "w" and data is not None:
        try:
            with open(file_path, mode, encoding="utf-8") as f:
                json.dump(data, f)
        except json.decoder.JSONDecodeError:
            log.warn("Failed to write json file...")
            return None
    else:
        raise ValueError("Invalid mode")
