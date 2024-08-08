class ToDoListManager:
    def __init__(self):
        self.tasks = {}

    def add_task(self, task_name):
        self.tasks[task_name] = 'Pending'

    def list_tasks(self):
        return self.tasks

    def mark_task_completed(self, task_name):
        if task_name in self.tasks:
            self.tasks[task_name] = 'Completed'

    def clear_tasks(self):
        self.tasks.clear()