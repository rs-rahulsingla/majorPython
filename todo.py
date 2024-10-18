import json

# Task class definition
class Task:
    def __init__(self, title, description, category):
        self.title = title
        self.description = description
        self.category = category
        self.completed = False

    def mark_completed(self):
        self.completed = True

# File handling to save tasks to JSON
def save_tasks(tasks):
    with open('tasks.json', 'w') as f:
        json.dump([task.__dict__ for task in tasks], f)

# File handling to load tasks from JSON
def load_tasks():
    try:
        with open('tasks.json', 'r') as f:
            return [Task(**data) for data in json.load(f)]
    except FileNotFoundError:
        return []

# Main menu for user interaction
def main():
    tasks = load_tasks()

    while True:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Completed")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Enter the task title: ")
            description = input("Enter the task description: ")
            category = input("Enter the task category (e.g., Work, Personal): ")
            tasks.append(Task(title, description, category))
        elif choice == '2':
            if not tasks:
                print("\nNo tasks available.")
            else:
                for idx, task in enumerate(tasks):
                    status = "Completed" if task.completed else "Pending"
                    print(f"\nTask {idx+1}: {task.title} | {task.category} | {status}")
                    print(f"Description: {task.description}")
        elif choice == '3':
            task_num = int(input("Enter task number to mark as completed: "))
            if 1 <= task_num <= len(tasks):
                tasks[task_num-1].mark_completed()
                print("Task marked as completed.")
            else:
                print("Invalid task number.")
        elif choice == '4':
            task_num = int(input("Enter task number to delete: "))
            if 1 <= task_num <= len(tasks):
                tasks.pop(task_num-1)
                print("Task deleted.")
            else:
                print("Invalid task number.")
        elif choice == '5':
            save_tasks(tasks)
            print("Tasks saved. Exiting.")
            break
        else:
            print("Invalid option. Please try again.")

# Run the main function
if __name__ == "__main__":
    main()
