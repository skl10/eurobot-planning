import Constants
from TaskCoordinator import TaskCoordinator

taskCoordinator = TaskCoordinator()
print(taskCoordinator.numIncompleteTasks)
print(taskCoordinator.GetRemainingTime())

for _ in range(Constants.TOTAL_TASKS):
    taskCoordinator.ExecuteNextTask()
    print(taskCoordinator.numIncompleteTasks)

print(taskCoordinator.GetRemainingTime())

