tasks = []

def add_task():
    task = input("Enter task name: ")
    tasks.append(task)
    print("Task added!\n")

def remove_task():
    print("Current tasks:")
    for i, task in enumerate(tasks):
        print(f"{i+1}. {task}")
    try:
        choice = int(input("Enter task number to remove: "))
        if 1 <= choice <= len(tasks):
            tasks.pop(choice - 1)
            print("Task removed!\n")
        else:
            print("Invalid task number!\n")
    except ValueError:
        print("Invalid input!\n")

def view_tasks():
    if len(tasks) == 0:
        print("No tasks found!\n")
    else:
        print("Current tasks:")
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")
        print()

while True:
    print("Welcome to the To-Do List Program!\n")
    print("Please select an option:")
    print("1. Add a task")
    print("2. Remove a task")
    print("3. View tasks")
    print("4. Exit\n")
    try:
        choice = int(input("Option: "))
        print()
        if choice == 1:
            add_task()
        elif choice == 2:
            remove_task()
        elif choice == 3:
            view_tasks()
        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid choice!\n")
    except ValueError:
        print("Invalid input!\n")
