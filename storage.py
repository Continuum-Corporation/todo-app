import json
import os

FILENAME = "tasks.json"

def load_tasks():
    """Load tasks from the JSON file."""
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            data = json.load(f)
            return data
    else:
        return []

def save_tasks(tasks):
    """Save tasks to the JSON file."""
    with open(FILENAME, "w") as f:
        json.dump(tasks, f)

def delete_tasks():
    """Delete all tasks stored in the JSON file."""
    if os.path.exists(FILENAME):
        os.remove(FILENAME)
    else:
        print("No tasks file found.")
