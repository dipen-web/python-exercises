# Step 1 - Define features

# 1. Add a task
# 2. View tasks
# 3. Mark a task as Done
# 4. Delete a task

# Step 2 - Data structure - decide how to store tasks in a program
# a list of dictionaries - each dictionary holds task details with id, task, done status

# Step 3 - Core functions - write small functions for each action.
tasks = []

def add_tasks(task_name):
    task_dict = {"id": len(tasks)+1, "task": task_name, "done": False}
    tasks.append(task_dict)
    print("✅ New task added succefully.\n")

def view_tasks():
    print("\n- All tasks:")
    for item in tasks:
        if item["done"]:
            print(f"☑ {item["task"]}")
        else:
            print(f"☐ {item["task"]}")
    print("\n")

def mark_done(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            print(f"Task '{task["task"]}' marked as completed ✔")
            return
    print("Task not found with this id.")

def delete_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            # remove that dictionary from the list
            del tasks[task_id-1]
            print(f"Task '{task["task"]}' deleted")
            print("\n- Updated task list:")
            view_tasks()
            return
    print("Task not found with this id.")

# Step 4 - Menu/CLI loop
# Create a loop to keep asking the user for input.

while True:

    print("------ To-do list CLI app -------")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark task as Done")
    print("4. Delete a task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # call respective functions based on choice
    if choice == "1":
        task_name = input("Enter task name: ")
        add_tasks(task_name)

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        task_id = int(input("Enter task id to mark as done: "))
        mark_done(task_id)

    elif choice == "4":
        task_id = int(input("Enter task id to delete: "))
        delete_task(task_id)

    elif choice == "5":
        print("Thank you for using our App! Have a good day!")
        break

    else:
        print("Please enter the correct choice!")

