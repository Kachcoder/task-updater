from models import Task

class TaskManager:
    def __init__(self):
        self.tasks = {}

    def add_task(self, task_id, title, priority="medium"):
        if task_id in self.tasks:
            raise ValueError(f"Task with ID {task_id} already exists.")
        task = Task(task_id, title, priority)
        self.tasks[task_id] = task
        return task

    def get_task(self, task_id):
        return self.tasks.get(task_id)

    def list_pending_tasks(self):
        return [t.to_dict() for t in self.tasks.values() if not t.completed]
