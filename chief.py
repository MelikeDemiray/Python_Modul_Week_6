from task_management import TaskManagement
from task_editing import TaskEditing
from task_tracking import TaskTracking


geciciListeElemanlari = "task bilgileri" # bu __str__ile taskden dondurulecek 

manager = TaskManagement()

edit = TaskEditing(manager,1) # liste ve id numarasi (gecici)
track = TaskTracking(manager,1) # liste ve id numarasi (gecicic)

manager.add_task(geciciListeElemanlari) 