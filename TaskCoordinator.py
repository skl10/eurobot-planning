import Constants
from time import time
from Tasks import *

class TaskCoordinator:

    def __init__(self):

        self.tasks = [BallTask(), BlockTask(), FlowerTask(), SwitchTask()]
        self.numIncompleteTasks = len(self.tasks)
        self.pointsEarned = 0
        self.startTime = time()
        self.endTime = self.startTime + Constants.TOTAL_TIME_LIMIT

    def GetRemainingTime(self):

        return self.endTime - time()

    def UpdateTimeLimits(self):

        # Simply diving remaining time equally amoung remaining tasks
        # Should probabaly do this differently
        remainingTime = self.GetRemainingTime()
        newTimeLimit = remainingTime / self.numIncompleteTasks

        for task in self.tasks:
            if task.performed is False:
                task.UpdateTimeLimit(newTimeLimit)

    def ExecuteNextTask(self):

        # Check if it's all been done
        if self.numIncompleteTasks == 0:
            return # Return an all complete flag?

        # Select the first incomplete task (this may not be the best way)
        for task in self.tasks:
            if task.performed is False:
                task.Execute()
                break

        # Change the time limits once a task has been executed
        self.UpdateTimeLimits()

        # Decrease number of incomplete tasks (success assumed)
        self.numIncompleteTasks -= 1
