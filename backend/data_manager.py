from logger import setup_logger


class DataManager:
    """Manage the data, send and retrieve portions of the data and convert to json"""

    def __init__(self, data: list):
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
