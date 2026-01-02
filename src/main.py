import sys
from typing import List, Optional

# --- 1. Task Class (Data Model) ---
class Task:
    """Represents a single to-do item."""
    def __init__(self, id: int, title: str, description: str, completed: bool = False):
        self.id = id
        self.title = title
        self.description = description
        self.completed = completed

    def __repr__(self) -> str:
        status = "Done" if self.completed else "Pending"
        return f"Task(id={self.id}, title='{self.title}', status='{status}')"

# --- 2. TodoManager Class (Business Logic) ---
class TodoManager:
    """Manages all the to-do list operations."""
    def __init__(self):
        self._tasks: List[Task] = []
        self._next_id: int = 1

    def add_task(self, title: str, description: str) -> Task:
        """Adds a new task to the list."""
        task = Task(id=self._next_id, title=title, description=description)
        self._tasks.append(task)
        self._next_id += 1
        return task

    def get_all_tasks(self) -> List[Task]:
        """Returns all tasks."""
        return self._tasks

    def find_task_by_id(self, task_id: int) -> Optional[Task]:
        """Finds a task by its ID."""
        for task in self._tasks:
            if task.id == task_id:
                return task
        return None

    def update_task(self, task_id: int, new_title: str, new_description: str) -> Optional[Task]:
        """Updates a task's title and description."""
        task = self.find_task_by_id(task_id)
        if task:
            task.title = new_title
            task.description = new_description
            return task
        return None

    def delete_task(self, task_id: int) -> bool:
        """Deletes a task by its ID."""
        task = self.find_task_by_id(task_id)
        if task:
            self._tasks.remove(task)
            return True
        return False

    def toggle_task_completion(self, task_id: int) -> Optional[Task]:
        """Toggles the completion status of a task."""
        task = self.find_task_by_id(task_id)
        if task:
            task.completed = not task.completed
            return task
        return None

# --- 3. UI Functions (Console Interface) ---

def print_menu():
    """Prints the main menu."""
    print("\n--- To-Do List Menu ---")
    print("1. Add a new task")
    print("2. View all tasks")
    print("3. Update a task")
    print("4. Delete a task")
    print("5. Mark a task as Done/Pending")
    print("6. Exit")
    print("-----------------------")

def view_tasks(manager: TodoManager):
    """Displays all tasks."""
    tasks = manager.get_all_tasks()
    if not tasks:
        print("No tasks found.")
        return
    print("\n--- All Tasks ---")
    for task in tasks:
        status = "Done" if task.completed else "Pending"
        print(f"ID: {task.id} | Title: {task.title} | Description: {task.description} | Status: {status}")
    print("-----------------")

def add_task(manager: TodoManager):
    """Handles adding a new task."""
    print("\n--- Add New Task ---")
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    if title and description:
        task = manager.add_task(title, description)
        print(f"Task '{task.title}' added successfully with ID {task.id}.")
    else:
        print("Title and description cannot be empty.")

def update_task(manager: TodoManager):
    """Handles updating a task."""
    print("\n--- Update Task ---")
    try:
        task_id = int(input("Enter the ID of the task to update: "))
        task = manager.find_task_by_id(task_id)
        if not task:
            print(f"Error: Task with ID {task_id} not found.")
            return

        print(f"Updating Task ID {task_id}. Current title: '{task.title}'")
        new_title = input(f"Enter new title (or press Enter to keep current): ") or task.title

        print(f"Current description: '{task.description}'")
        new_description = input(f"Enter new description (or press Enter to keep current): ") or task.description

        manager.update_task(task_id, new_title, new_description)
        print("Task updated successfully.")

    except ValueError:
        print("Invalid input. Please enter a valid number for the task ID.")

def delete_task(manager: TodoManager):
    """Handles deleting a task."""
    print("\n--- Delete Task ---")
    try:
        task_id = int(input("Enter the ID of the task to delete: "))
        if manager.delete_task(task_id):
            print(f"Task with ID {task_id} deleted successfully.")
        else:
            print(f"Error: Task with ID {task_id} not found.")
    except ValueError:
        print("Invalid input. Please enter a valid number for the task ID.")

def toggle_task(manager: TodoManager):
    """Handles toggling a task's completion status."""
    print("\n--- Toggle Task Completion ---")
    try:
        task_id = int(input("Enter the ID of the task to toggle: "))
        task = manager.toggle_task_completion(task_id)
        if task:
            status = "Done" if task.completed else "Pending"
            print(f"Task '{task.title}' (ID: {task.id}) marked as {status}.")
        else:
            print(f"Error: Task with ID {task_id} not found.")
    except ValueError:
        print("Invalid input. Please enter a valid number for the task ID.")

# --- 4. Main Application Loop ---
def main():
    """Main function to run the application."""
    manager = TodoManager()
    while True:
        print_menu()
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_task(manager)
        elif choice == '2':
            view_tasks(manager)
        elif choice == '3':
            update_task(manager)
        elif choice == '4':
            delete_task(manager)
        elif choice == '5':
            toggle_task(manager)
        elif choice == '6':
            print("Exiting the application. Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
