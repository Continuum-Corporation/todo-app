from datetime import datetime

class Task:
    def __init__(self, title, description='', due_date=None, completed=False):
        self.title = title
        self.description = description
        self.created_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.due_date = due_date
        self.completed = completed

    def __str__(self):
        return f"{self.title} ({'completed' if self.completed else 'pending'})"

    def to_dict(self):
        """Convert the Task object to a dictionary."""
        return {
            "title": self.title,
            "description": self.description,
            "created_at": self.created_at,
            "due_date": self.due_date,
            "completed": self.completed
        }

    @classmethod
    def from_dict(cls, task_dict):
        """Create a Task object from a given dictionary."""
        return cls(
            title=task_dict["title"],
            description=task_dict["description"],
            due_date=task_dict["due_date"],
            completed=task_dict["completed"]
        )

