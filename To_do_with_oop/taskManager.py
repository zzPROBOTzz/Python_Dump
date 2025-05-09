class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task":task, "complete" : False})

    def remove_task(self, task):
        self.tasks = [ t for t in  self.tasks if t["task"] != task]

    def complete_task(self, task):
        for t in self.tasks:
            if t["task"] == task:
                t["completed"] = True

    def list_task(self):
        if not self.tasks:
            print("NO TASK AVAILABLE")
        else:
            for i, t in enumerate(self.tasks, 1):
                status = "good" if t["completed"] else "not good"
                print(f"{i}. {status} {t['task']}")