class Task():

    def __init__(self, timeLimit):
        self.timeLimit = timeLimit
        self.performed = False

    def Execute(self):
        pass

class BallTask(Task):

    def __init__(self, timeLimit):
        super().__init__(timeLimit)

    def Execute(self):

        self.performed = True
