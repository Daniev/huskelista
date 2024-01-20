from data_manager import DataManager, FilePaths


if __name__ == "__main__":
    # Used to generate test data when running github workflows.
    fp = FilePaths("./data/tasks.json")
    dm = DataManager(fp)
    dm.ensure_data_setup()
    dm.generate_test_tasks()
