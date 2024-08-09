class ToDoListManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        """Add a new task to the to-do list."""
        self.tasks.append({'task': task, 'status': 'Pending'})

    def list_tasks(self):
        """List all tasks with their statuses."""
        return self.tasks

    def mark_task_as_completed(self, task):
        """Mark a specified task as completed."""
        for t in self.tasks:
            if t['task'] == task:
                t['status'] = 'Completed'
                return
        raise ValueError(f'Task "{task}" not found.')

    def clear_tasks(self):
        """Clear the entire to-do list."""
        self.tasks = []


# Example usage
if __name__ == "__main__":
    manager = ToDoListManager()

    # Add some tasks
    manager.add_task("Buy groceries")
    manager.add_task("Pay bills")

    # List tasks
    print("Tasks:", manager.list_tasks())

    # Mark a task as completed
    manager.mark_task_as_completed("Buy groceries")
    print("Tasks after marking as completed:", manager.list_tasks())

    # Clear tasks
    manager.clear_tasks()
    print("Tasks after clearing:", manager.list_tasks())
