from logger import setup_logger
from utils import open_json, generate_slug
from data_setup import TASK_FILE


class DataManager:
    """Manage the data, send and retrieve portions of the data and convert to json"""

    def __init__(self, data: list = []):
        self.data: list = data
        self.log = setup_logger()

    def get_tasks_by_user(self, user: str) -> list:
        tasks = [task for task in self.data if task["assignee"].lower() == user.lower()]
        return tasks

    def get_task_by_slug(self, slug) -> dict:
        for task in self.data:
            if task["slug"] == slug:
                return task
        return None

    def add_task_to_file(self, task) -> None:
        """Generates a slug and add task to json file"""
        task["slug"] = generate_slug(task["title"])
        tasks = open_json(TASK_FILE, "r")
        if tasks:
            tasks.append(task)
        else:
            tasks = [task]
        open_json(TASK_FILE, "w", tasks)
