from datetime import datetime

class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = datetime.strptime(due_date, '%Y-%m-%d') 
        self.status = False

    def mark_complete(self):
        self.status = True

    def __str__(self):
        status_str = "Complete" if self.status else "Incomplete"
        return f"Task: {self.title}\nDescription: {self.description}\nDue: {self.due_date.date()}\nStatus: {status_str}"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task.title}' added.")

    def mark_task_complete(self, title):
        for task in self.tasks:
            if task.title.lower() == title.lower():
                task.mark_complete()
                print(f"Task '{title}' marked as complete.")
                return True
        print(f"Task '{title}' not found.")
        return False

    def list_all_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
            return
        print("All Tasks:")
        for task in self.tasks:
            print("-" * 20)
            print(task)

    def list_incomplete_tasks(self):
        incomplete_tasks = [task for task in self.tasks if not task.status]
        if not incomplete_tasks:
            print("No incomplete tasks.")
            return
        print("Incomplete Tasks:")
        for task in incomplete_tasks:
            print("-" * 20)
            print(task)

def main():
    todo = ToDoList()

    # Pre-populate with some test tasks (optional)
    todo.add_task(Task("Buy groceries", "Milk, Bread, Eggs", "2025-08-10"))
    todo.add_task(Task("Finish homework", "Complete math exercises", "2025-08-07"))

    while True:
        print("\n--- ToDo List Menu ---")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. List All Tasks")
        print("4. List Incomplete Tasks")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Task Title: ").strip()
            description = input("Description: ").strip()
            due_date = input("Due Date (YYYY-MM-DD): ").strip()
            try:
                task = Task(title, description, due_date)
                todo.add_task(task)
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")

        elif choice == '2':
            title = input("Enter task title to mark complete: ").strip()
            todo.mark_task_complete(title)

        elif choice == '3':
            todo.list_all_tasks()

        elif choice == '4':
            todo.list_incomplete_tasks()

        elif choice == '5':
            print("Exiting ToDo List. Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()


