class Task:
    def __init__(self, task_id, title, description, status="To Do"):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.status = status

    def __str__(self):
        return f"Task {self.task_id}: {self.title} - Status: {self.status}"

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description):
        task_id = len(self.tasks) + 1
        task = Task(task_id, title, description)
        self.tasks.append(task)

    def remove_task(self, task_id):
        task_to_remove = None
        for task in self.tasks:
            if task.task_id == task_id:
                task_to_remove = task
                break
        if task_to_remove:
            self.tasks.remove(task_to_remove)

    def list_tasks(self):
        for task in self.tasks:
            print(task)

    def mark_task_done(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                task.status = "Done"
                break

if __name__ == "__main__":
    task_manager = TaskManager()

    while True:
        print("\nTask Manager Menu:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. List Tasks")
        print("4. Mark Task as Done")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            task_manager.add_task(title, description)
        elif choice == "2":
            task_id = int(input("Enter task ID to remove: "))
            task_manager.remove_task(task_id)
        elif choice == "3":
            print("\nList of Tasks:")
            task_manager.list_tasks()
        elif choice == "4":
            task_id = int(input("Enter task ID to mark as Done: "))
            task_manager.mark_task_done(task_id)
        elif choice == "5":
            print("Exiting Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
