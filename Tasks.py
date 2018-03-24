import Constants
from Colours import Colours
from Coordinates import Coordinates
from random import randint

class Task():

    def __init__(self, timeLimit=Constants.TOTAL_TIME_LIMIT/Constants.TOTAL_TASKS):
        self.timeLimit = timeLimit
        self.performed = False

    def GetCurrentLocation(self):
        return Coordinates(1,1,1)

    def CoordinateMove(self,coords):
        pass

    def RelativeMove(self,x,y,z):

        # Move relative to current location
        destination = self.GetCurrentLocation()

        destination.x += x
        destination.y += y
        destination.z += z

        self.CoordinateMove(destination)

    def IdentifyColour(self):
        someColour = Colours(randint(1,5))
        return someColour

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

    def ReadBuildingPlan(self):

        # Some tiny change in X used to move to the next colour on the building plan
        shiftX = 0.1

        for i in range(Constants.BUILDING_HEIGHT):
            self.BuildingPlan[i] = self.IdentifyColour()
            self.RelativeMove(shiftX,0,0)

    def CollectBlocks(self):

        # Push as many blocks as possible to the assembly location
        self.ExtendArms()
        self.CoordinateMove(Constants.ASSEMBLY_LOCATION)

    def ConstructBuilding(self, depth=0):
        pass

    def Execute(self):

        # Navigate to the area where the Blocks are kept
        self.CoordinateMove(Constants.BLOCK_LOCATION)

        # Move blocks to assembly area
        self.CollectBlocks()

        # Examine the building plan
        self.CoordinateMove(Constants.BUILDING_PLAN_LOCATION)

        # Try until the result is at least an array of unique colours
        while (len(set(self.BuildingPlan)) is not Constants.BUILDING_HEIGHT):
            self.ReadBuildingPlan()

        # Move to building area once plan is known
        self.CoordinateMove(Constants.ASSEMBLY_LOCATION)

        # Construct a Building
        self.ConstructBuilding(self)

        print(self.BuildingPlan)
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
