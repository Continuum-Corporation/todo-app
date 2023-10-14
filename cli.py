import argparse
from todolist import ToDoList

def main():
    parser = argparse.ArgumentParser(description="Manage your To-Do List")

    subparsers = parser.add_subparsers(dest="command")

    # Add Task
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("title", help="Title of the task")
    add_parser.add_argument("-d", "--description", help="Description of the task", default="")
    add_parser.add_argument("-D", "--due_date", help="Due date of the task (YYYY-MM-DD)", default=None)

    # Remove Task
    remove_parser = subparsers.add_parser("remove", help="Remove a task by index")
    remove_parser.add_argument("index", type=int, help="Index of the task to remove")

    # Mark Task as Completed
    complete_parser = subparsers.add_parser("complete", help="Mark a task as completed by index")
    complete_parser.add_argument("index", type=int, help="Index of the task to mark as completed")

    # View tasks
    view_parser = subparsers.add_parser("view", help="View tasks")
    view_parser.add_argument("-s", "--status", choices=["all", "pending", "completed", "overdue"],
                             help="Filter tasks by status", default="all")

    args = parser.parse_args()

    todo_list = ToDoList()

    if args.command == "add":
        todo_list.add_task(args.title, args.description, args.due_date)
        print("Task added successfully.")
    elif args.command == "remove":
        todo_list.remove_task(args.index)
        print("Task removed successfully.")
    elif args.command == "complete":
        todo_list.mark_as_completed(args.index)
        print("Task marked as completed.")
    elif args.command == "view":
        tasks = []
        if args.status == "all":
            tasks = todo_list.tasks
        elif args.status == "pending":
            tasks = todo_list.get_pending_tasks()
        elif args.status == "completed":
            tasks = todo_list.get_completed_tasks()
        elif args.status == "overdue":
            tasks = todo_list.get_overdue_tasks()

        print("Tasks:")
        for i, task in enumerate(tasks):
            print(f"{i}: {task}")

if __name__ == "__main__":
    main()
