def display_menu():
    print("\nTo-Do List Application")
    print("1. Add Tasks")
    print("2. Show Tasks")
    print("3. Delete Task")
    print("4. EXIT")

def add_task(tasks):
    n_tasks = int(input("How many tasks do you want to add? "))

    for i in range(n_tasks):
        task = input("Enter the task: ")
        tasks.append(task)
        print("Task added!")

def show_tasks(tasks):

    if not tasks:
        print("No tasks available.")
    else:
        print("\nTo-Do List:")
        for index, task in enumerate(tasks, 1):
            print(f"{index}. {task}")

def delete_task(tasks):

    show_tasks(tasks)

    if tasks:

        try:
            task_num = int(input("Enter the task number to delete: "))
            if 1 <= task_num <= len(tasks):
                removed_task = tasks.pop(task_num - 1)
                print(f"Task '{removed_task}' deleted.")
            else:
                print("Invalid task number.")

        except ValueError:
            print("Please enter a valid number.")

def main():

    tasks = []

    while True:
        display_menu()
        choice = input("Choose an option: ")
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            show_tasks(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main()
