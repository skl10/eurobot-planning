import Constants

class Task():

    def __init__(self, timeLimit=Constants.TOTAL_TIME_LIMIT/Constants.TOTAL_TASKS):
        self.timeLimit = timeLimit
        self.performed = False

    def GetCurrentLocation()
        pass

    def Move(coords):
        pass

    def OffsetMove(x,y,z):

        destination = self.GetCurrentLocation()

        destination.x += x
        destination.y += y
        destination.z += z

        self.Move(destination)

    def CoordinateMove():

        destination = Coordinates(x,y,z)
        self.Move(destination)

    def UpdateTimeLimit(self, newTimeLimit):

        # If certain tasks are completed earlier/later than expected then the timelimit is updated
        self.timeLimit = newTimeLimit

    def Execute(self):
        pass

class BallTask(Task):

    def __init__(self, timeLimit=Constants.INIT_BALL_LIMIT):
        super().__init__(timeLimit)

    def Execute(self):

        # Do stuff
        self.performed = True

class BlockTask(Task):

    def __init__(self, timeLimit=Constants.INIT_BLOCK_LIMIT):
        super().__init__(timeLimit)

    def CollectBlocks(self):
        pass

    def Execute(self):

        # Do stuff
        self.performed = True

class FlowerTask(Task):

    def __init__(self, timeLimit=Constants.INIT_FLOWER_LIMIT):
        super().__init__(timeLimit)

    def Execute(self):

        # Do stuff
        self.performed = True

class SwitchTask(Task):

    def __init__(self, timeLimit=Constants.INIT_SWITCH_LIMIT):
        super().__init__(timeLimit)

    def Execute(self):

        # Do stuff
        self.performed = True
