from abc import ABC, abstractmethod

class Task(ABC):
    def __init__(self, task_id, task_name, deadline, color, status="Pending", priority="Low"):
        self.task_id = task_id
        self.task_name = task_name
        self.deadline = deadline # deadline olusturulacak
        self.status = status
        self.priority = priority
        self.color = color

    @abstractmethod # alt siniflarin kullanmasi mecbur
    def color_your_task(self):
        pass

    def days_to_accomplish_task(self):
        pass

# str eklenecek donen deger managementdeki listeye atilacak(management icinde)
class PersonalTask(Task):
    pass
class WorkTask(Task):
    pass