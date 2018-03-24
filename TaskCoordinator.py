import Constants

class TaskCoordinator:

    def __init__(self):

        self.tasks = [BallTask(), BlockTask(), FlowerTask(), ]

    def SelectTask(self):

        for task in self.tasks:
            if task.performed is False:
                return task.Execute()

        return -1

    def BallTask(self):

        self.performedTask[ballTaskIndex] = True

    def BlockTask(self):

        self.performedTask[blockTaskIndex] = True
