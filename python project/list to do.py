tasks = []

def add_task():
    print("\n Add Task ")
    title = input("Enter task title: ")
    tasks.append({"title": title, "done": False})
    print("Task added.\n")


def view_tasks():
    print("\n To-Do List ")
    if not tasks:
        print("No tasks added.\n")
        return

    for i, t in enumerate(tasks, start=1):
        status = "Done" if t["done"] else "Pending"
        print(f"{i}. {t['title']}  [{status}]")
    print()


def mark_done():
    view_tasks()
    if not tasks:
        return
    num = int(input("Enter task number to mark as done: "))
    if 1 <= num <= len(tasks):
        tasks[num - 1]["done"] = True
        print("Task marked as done.\n")
    else:
        print("Invalid task number.\n")


def main():
    while True:
        print(" To-Do List Manager ")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Exit")

        ch = input("Enter your choice (1-4): ")

        if ch == "1":
            add_task()
        elif ch == "2":
            view_tasks()
        elif ch == "3":
            mark_done()
        elif ch == "4":
            print("Exiting To-Do List Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main()