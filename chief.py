from task import PersonalTask, WorkTask
from task_management import TaskManagement
from task_editing import TaskEditing
from task_tracking import TaskTracking


task_manager = TaskManagement()

edit = TaskEditing(task_manager,1) # liste ve id numarasi (gecici)
track = TaskTracking(task_manager,1) # liste ve id numarasi (gecicic)