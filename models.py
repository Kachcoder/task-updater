class Task:
    def __init__(self, task_id, title, priority="medium"):
        self.task_id = task_id
        self.title = title
        self.priority = priority
        self.completed = False

    def mark_complete(self):
        self.completed = True

    def to_dict(self):
        return {
            "id": self.task_id,
            "title": self.title,
            "priority": self.priority,
            "completed": self.completed
        }
