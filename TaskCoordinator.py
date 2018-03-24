import Constants
from Tasks import Task

class TaskCoordinator:

    def __init__(self):

        self.tasks = [BallTask(), BlockTask(), FlowerTask(), SwitchTask()]
        self.numIncompleteTasks = len(self.tasks)

    def UpdateTimeLimits(self):

        for task in self.tasks:
            if task.performed is False
                task.UpdateTimeLimit()

    def SelectTask(self):

        # Check if it's all been done
        if self.numIncompleteTasks == 0:
            return

        # Select the first incomplete task (this may not be the best way)
        for task in self.tasks:
            if task.performed is False:
                task.Execute()
                break

        # Change the time limits once a task has been executed
        self.UpdateTimeLimits()

        # Decreate number of inomplete tasks
        self.numIncompleteTasks -= 1
