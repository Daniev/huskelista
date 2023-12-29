"""Test the data manager class"""
import pytest
from data_manager import DataManager, FilePaths


@pytest.fixture
def filepaths():
    return FilePaths("./testdata/tasks.json")


@pytest.fixture
def dm(filepaths):
    dm = DataManager(filepaths)
    dm.ensure_data_setup("./testdata")
    dm.generate_test_tasks()
    return dm


@pytest.fixture(scope="module")
def cleanup_after_test(request, filepaths):
    def cleanup():
        # remove the test data...
        dm = DataManager(filepaths)
        dm.wipe_existing_data("./testdata")

    request.addFinalizer(cleanup)


def test_get_tasks(dm):
    result = dm.get_tasks()
    assert result is not None
    assert len(result) > 0


def test_get_task_by_slug_empty(dm):
    result = dm.get_task_by_slug("")
    assert result is None


def test_get_task_by_slug(dm):
    tasks = dm.get_tasks()
    result = dm.get_task_by_slug(tasks[0]["slug"])
    assert result is not None
    assert result == tasks[0]


def test_get_task_by_slug_invalid(dm):
    result = dm.get_task_by_slug("invalid")
    assert result is None


def test_get_tasks_by_user(dm):
    result = dm.get_tasks_by_user("daniel")
    assert result is not None
    assert len(result) > 0


def test_get_tasks_by_user_invalid(dm):
    result = dm.get_tasks_by_user("invalid")
    assert result is None


def test_add_task_to_file(dm):
    task = {"title": "testAdd", "assignee": "daniel", "complete": False}
    dm.add_task_to_file(task)
    tasks = dm.get_tasks()
    assert task in tasks


def test_delete_task(dm):
    task = dm.get_tasks()[0]
    dm.delete_task(task["slug"])
    tasks = dm.get_tasks()
    assert task not in tasks
