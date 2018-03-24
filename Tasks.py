import Constants

class Task():

    def __init__(self, timeLimit=Constants.TOTAL_TIME_LIMIT/Constants.TOTAL_TASKS):
        self.timeLimit = timeLimit
        self.performed = False

    def GetCurrentLocation(self):
        pass

    def CoordinateMove(self,coords):
        pass

    def OffsetMove(self,x,y,z):

        # Move relative to current location
        destination = self.GetCurrentLocation()

        destination.x += x
        destination.y += y
        destination.z += z

        self.Move(destination)

    def Pick(self):
        pass

    def Release(self):
        pass

    def Place(self):
        pass

    def ExtendArms(self):
        pass

    def CloseArms(self):
        pass

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
        self.BuildingPlan = [None, None, None]

    def CollectBlocks(self):
        pass

    def Execute(self):

        # Navigate to the area where the Blocks are kept
        self.CoordinateMove(Constants.BLOCK_LOCATION)

        # Push as many blocks as possible to the assembly location
        self.ExtendArms()
        self.CoordinateMove(Constants.ASSEMBLY_LOCATION)

        # Examine the building plan
        self.CoordinateMove(Constants.BUILDING_PLAN_LOCATION)

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
