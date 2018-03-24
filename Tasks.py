class Task():

    def __init__(self, timeLimit):
        self.timeLimit = timeLimit
        self.performed = False

    def UpdateTimeLimit(self, newTimeLimit):

        # If certain tasks are completed earlier/later than expected then the timelimit is updated
        self.timeLimit = newTimeLimit

    def Execute(self):
        pass

class BallTask(Task):

    def __init__(self, timeLimit):
        super().__init__(timeLimit)

    def Execute(self):

        # Do stuff
        self.performed = True

class BlockTask(Task):

    def __init__(self, timeLimit):
        super().__init__(timeLimit)

    def Execute(self):

        # Do stuff
        self.performed = True

class FlowerTask(Task):

    def __init__(self, timeLimit):
        super().__init__(timeLimit)

    def Execute(self):

        # Do stuff
        self.performed = True

class SwitchTask(Task):

    def __init__(self, timeLimit):
        super().__init__(timeLimit)

    def Execute(self):

        # Do stuff
        self.performed = True
