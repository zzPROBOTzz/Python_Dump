
import json
from taskManager import TaskManager

class FileTaskManager(TaskManager):
    def __init__(self, filename = "task.json"):
        super().__init__()
        self.filename = filename
        self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.filename, "r") as f:
                data = json.load(f)
                if isinstance(data, list):
                    self.tasks = data
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_tasks(self):
        with open(self.filename, "w") as f:
            json.dump(self.tasks, f, indent=4)

    def add_task(self, task):
        super().add_task(task)
        self.save_tasks()

    def remove_task(self, task):
        super().remove_task(task)
        self.save_tasks()

    def complete_task(self, task):
        super().complete_task(task)
        self.save_tasks()