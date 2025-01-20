class TaskManagement:
    def __init__(self):
        self.tasks = []

    def add_task(self,task):
        if task not in self.tasks:
            self.tasks.append(task)
            print("Task added successfully!")

    def print_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        for task in self.tasks:
            print(task)