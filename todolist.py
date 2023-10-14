from task import Task
import storage

class ToDoList:
    def __init__(self):
        self.tasks = [Task.from_dict(task_data) for task_data in storage.load_tasks()]

    def add_task(self, title, description='', due_date=None):
        task = Task(title, description, due_date)
        self.tasks.append(task)
        storage.save_tasks([task.to_dict() for task in self.tasks])

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            storage.save_tasks([task.to_dict() for task in self.tasks])
        else:
            print("Invalid task index.")

    def mark_as_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed = True
            storage.save_tasks([task.to_dict() for task in self.tasks])
        else:
            print("Invalid task index.")

    def get_pending_tasks(self):
        return [task for task in self.tasks if not task.completed]

    def get_completed_tasks(self):
        return [task for task in self.tasks if task.completed]

    def get_overdue_tasks(self):
        overdue_tasks = []
        for task in self.tasks:
            if task.due_date and not task.completed:
                task_due_date = datetime.strptime(task.due_date, '%Y-%m-%d')
                if datetime.now() > task_due_date:
                    overdue_tasks.append(task)
        return overdue_tasks

    def display_tasks(self):
        if len(self.tasks) == 0:
            print("No tasks available.")
            return
        print("Tasks:")
        for i, task in enumerate(self.tasks):
            print(f"{i}: {task}")
