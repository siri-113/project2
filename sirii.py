 #Simple To-Do List Application

# Create an empty list to store tasks
tasks = []

def show_menu():
    print("\n--- To-Do List Menu ---")
    print("1. View tasks")
    print("2. Add a task")
    print("3. Mark a task as done")
    print("4. Delete a task")
    print("5. Exit")

def view_tasks():
    if not tasks:
        print("\nNo tasks in the list.")
    else:
        print("\n--- To-Do List ---")
        for i, task in enumerate(tasks, start=1):
            status = "Done" if task["done"] else "Not Done"
            print(f"{i}. {task['title']} - [{status}]")

def add_task():
    title = input("\nEnter the task title: ")
    task = {"title": title, "done": False}
    tasks.append(task)
    print("Task added successfully!")

def mark_task_as_done():
    view_tasks()
    task_num = int(input("\nEnter the task number to mark as done: ")) - 1
    if 0 <= task_num < len(tasks):
        tasks[task_num]["done"] = True
        print("Task marked as done!")
    else:
        print("Invalid task number.")

def delete_task():
    view_tasks()
    task_num = int(input("\nEnter the task number to delete: ")) - 1
    if 0 <= task_num < len(tasks):
        tasks.pop
