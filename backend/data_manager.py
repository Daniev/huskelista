from logger import setup_logger
from utils import open_json, generate_slug
import os


class FilePaths:
    """Contains file paths for the data files, Exists to allow for testing files"""

    TASK_FILE = "./data/tasks.json"

    def __init__(self, taskFile: str) -> None:
        self.TASK_FILE = taskFile

    def values(self):
        return [self.TASK_FILE]


class DataManager:
    """Manage the data, send and retrieve portions of the data and convert to json"""

    def __init__(self, filepaths: FilePaths):
        self.log = setup_logger()
        self.filepaths: FilePaths = filepaths

    def get_tasks(self):
        """Gets all tasks from json file"""
        tasks = open_json(self.filepaths.TASK_FILE, "r")
        if tasks == []:
            tasks = None
        return tasks

    def get_tasks_by_user(self, user: str) -> list:
        tasks = self.get_tasks()
        if user is not None and tasks is not None:
            tasks = [task for task in tasks if task["assignee"].lower() == user.lower()]
        if tasks == []:
            tasks = None
        return tasks

    def get_task_by_slug(self, slug) -> dict:
        tasks = self.get_tasks()
        for task in tasks:
            if task["slug"] == slug:
                return task
        return None

    def add_task_to_file(self, task) -> None:
        """Generates a slug and add task to json file"""
        if task == [] or task is None:
            self.log.warn("Empty task")
            return
        task["slug"] = generate_slug(task["title"])
        tasks = self.get_tasks()
        if tasks is not None:
            tasks.append(task)
        else:
            tasks = [task]
        open_json(self.filepaths.TASK_FILE, "w", tasks)

    def delete_task(self, slug):
        tasks = self.get_tasks()
        new_tasks = [task for task in tasks if task["slug"] != slug]
        open_json(self.filepaths.TASK_FILE, "w", new_tasks)

    def ensure_data_setup(self, data_folder_path="./data"):
        """Ensure that a data folder and the files exists. If not, create them."""
        status = False
        if os.path.exists(data_folder_path):
            pass
        else:
            self.log.info(f"Creating data folder at {data_folder_path}")
            os.mkdir(data_folder_path)
            status = True

        for json_file in self.filepaths.values():
            if os.path.exists(json_file):
                pass
            else:
                self.log.info(f"Creating {json_file} file")
                status = True
                with open(json_file, "w"):
                    pass

        self.log.info("Data setup complete")
        return status

    def wipe_existing_data(self, directory="./data"):
        """Deletes the content of the data folder, to start on a clean slate"""
        self.log.warn("Wiping existing data")
        if not os.path.exists("./data"):
            return
        for json_file in self.filepaths.values():
            os.remove(json_file)
        os.rmdir(directory)

    def generate_test_tasks(self):
        """Generates test tasks and stores them in the tasks.json file"""
        tasks = []
        tasks.append(
            {
                "slug": generate_slug("Støvsug sofa"),
                "title": "Støvsug sofa",
                "assignee": "Daniel",
                "complete": False,
            }
        )
        tasks.append(
            {
                "slug": generate_slug("Vask bad"),
                "title": "Vask bad",
                "assignee": "Daniel",
                "complete": False,
            }
        )
        tasks.append(
            {
                "slug": generate_slug("Klesvask"),
                "title": "Klesvask",
                "assignee": "Mia",
                "complete": False,
            }
        )
        tasks.append
        (
            {
                "slug": generate_slug("Vaske ovn og kjøleskap"),
                "title": "Vaske ovn og kjøleskap",
                "assignee": "Mia",
                "complete": False,
            }
        )
        tasks.append(
            {
                "slug": generate_slug("Sengetøy og re opp seng"),
                "title": "Sengetøy og re opp seng",
                "assignee": "Mia",
                "complete": True,
            }
        )

        tasks.append(
            {
                "slug": generate_slug("Vaske kjøkken"),
                "title": "Vaske kjøkken",
                "assignee": "Mia",
                "complete": True,
            }
        )
        open_json(self.filepaths.TASK_FILE, "w", tasks)
        return
