import os
from logger import setup_logger
from utils import generate_slug, open_json


data_folder_path = "./data"
json_files = ("tasks.json", "users.json")
log = setup_logger()


def ensure_data_setup():
    """Ensure that a data folder and the files exists. If not, create them."""

    if os.path.exists(data_folder_path):
        pass
    else:
        log.info(f"Creating data folder at {data_folder_path}")
        os.mkdir(data_folder_path)

    for json_file in json_files:
        if os.path.exists(f"{data_folder_path}/{json_file}"):
            pass
        else:
            log.info(f"Creating {json_file} file")
            with open(f"{data_folder_path}/{json_file}", "w"):
                pass

    log.info("Data setup complete")
    pass


def wipe_existing_data():
    """Deletes the content of the data folder, to start on a clean slate"""
    log.warn("Wiping existing data")
    if not os.path.exists(data_folder_path):
        return
    for json_file in json_files:
        os.remove(f"{data_folder_path}/{json_file}")
    os.rmdir(data_folder_path)


def generate_test_tasks():
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
    open_json(f"{data_folder_path}/tasks.json", "w", tasks)
    return
