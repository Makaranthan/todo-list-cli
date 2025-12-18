tasks = []

def add_task():
    task = input("Enter task: ")
    tasks.append(task)
    print("Task added")

def view_tasks():
    if not tasks:
        print("No tasks available")
        return
    for i in range(len(tasks)):
        print(i + 1, ".", tasks[i])

def delete_task():
    view_tasks()
    index = int(input("Enter task number to delete: "))
    if 1 <= index <= len(tasks):
        tasks.pop(index - 1)
        print("Task deleted")
    else:
        print("Invalid task number")

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        add_task()
    elif choice == 2:
        view_tasks()
    elif choice == 3:
        delete_task()
    elif choice == 4:
        break
    else:
        print("Invalid choice")
      
