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

    def Place(self, depth):
        """ Place a block at given depth (0 = ground, 1 = on top of 1 other block, etc.
        We might want to change this to be a more specific x y z location
        """
        pass

    def ExtendArms(self):
        pass

    def CloseArms(self):
        pass

    def Rotate(self, angle):
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
        self.buildingPlan = [None for _ in range(Constants.BUILDING_HEIGHT)]

    def ReadBuildingPlan(self):

        # Some tiny change in X used to move to the next colour on the building plan
        shiftX = 0.1

        for i in range(Constants.BUILDING_HEIGHT):
            self.buildingPlan[i] = self.IdentifyColour()
            self.RelativeMove(shiftX,0,0)

    def CollectBlocks(self):

        # Push as many blocks as possible to the assembly location
        self.ExtendArms()
        self.CoordinateMove(Constants.ASSEMBLY_LOCATION)
        self.CloseArms()

    def ValidBuildingPlan(self):

        if (len(set(self.buildingPlan)) is not Constants.BUILDING_HEIGHT):
            return False

        if (Colours.GOLD in self.buildingPlan):
            return False

        return True

    def RetrieveBlock(self, colour):
        # Pick a block based on its colour
        pass

    def AnyRetrieveBlock(self, colour):
        # Pick the first visible block
        pass

    def LookForBlock(self, colour):

        if (self.BlockAvaliable(colour)):
            # Pick the block with the correct colour
            self.RetrieveBlock(colour)
        elif (self.BlockAvaliable(Colours.GOLD)):
            # Pick the gold block
            RetrieveBlock(Colours.GOLD)
        elif (self.AnyBlockAvaliable()):
            # Pick whatever block is there
            AnyRetrieveBlock()
        else:
            # Can't find anything
            pass

    def ConstructBuilding(self, depth=0):
        
        depth = 0

        # simplified for now
        for i in range(1, Constants.BUILDING_HEIGHT):
            RetrieveBlock(buildingColours[i])
            Place(depth) # CHANGE THIS TO REFLECT WHERE THE BLOCK IS
            depth++

    def Execute(self):

        # Examine the building plan
        self.CoordinateMove(Constants.BUILDING_PLAN_LOCATION)

        # Try until the result is at least an array of unique colours
        while (not self.ValidBuildingPlan()):
            self.ReadBuildingPlan()
            # self.MoveBackToFaceFirstSquareOfBuildingPlan() ?

        # Just to see what happened
        print(self.buildingPlan)

        # Navigate to the area where the Blocks are kept
        self.CoordinateMove(Constants.BLOCK_LOCATION)

        # Move blocks to assembly area
        self.CollectBlocks()

        # Move to building area once plan is known
        self.CoordinateMove(Constants.ASSEMBLY_LOCATION)

        # Construct a Building
        self.ConstructBuilding(self)

        # Assume success
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
