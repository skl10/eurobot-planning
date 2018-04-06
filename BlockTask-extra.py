import Constants

# TO DO: Make strategy more precise in terms of what to do when 
#        we don't have the right blocks, how long to spend looking for
#        the right blocks, how many blocks to collect, etc. 

def DetermineOrder():
	"""Assuming robot is already looking at first square of 
	construction plan, identify the colours of all three squares.
	Returns a list of the three colours. 
	"""

	smallx = 0.5
	# PLACEHOLDER - smallx is how much the robot shifts to see the next square
	buildingColours[0] = IdentifyColour()

	for i in range(1, Constants.BUILDING_HEIGHT):
	# note: why use building height here? will we always build 3 height? 
		Shift(smallx)
		# Rotation necessary?
		buildingColours[i] = IdentifyColour()

	return buildingColours

def CollectBlocks():
	"""Push as many blocks as possible into the construction area."""

	int blocksPicked = 0

	while (VisibleBlocks() && blocksPicked < Constants.BLOCK_CAPACITY):
		GoToBlocks()
		ExtendFlaps()
		PushBlocks()
		# blocksPicked should be updated during one of these... 
		# need vision to count and push blocks

def AssembleBuilding():
	"""Stack BUILDING_HEIGHT blocks on top of each other in the 
	order described by the plan.
	"""

	depth = 0

	for i in range(1, Constants.BUILDING_HEIGHT):
		RetrieveBlock(buildingColours[i])
		PlaceBlock(depth)
		depth++

def RetrieveBlock(col):
	"""Look for the desired colour block, and if it's not there,
	take one that is.
	"""

	if (!BlockAvailable(col)):
		if (BlockAvailable(GOLD)):
			col = GOLD
		else if (AnyBlocksAvailable()):
			col = AVAILABLE_COLOUR
		else:
			# error
			return

	PickBlock(col)

def BuildingsTask(timeLimit):

	while (timePassed < timeLimit):

		NavigateTo(Constants.BUILDING_PLAN_LOCATION)
		buildingColours = DetermineOrder() 

		NavigateTo(Constants.BLOCK_LOCATION)
		CollectBlocks()
		NavigateTo(Constants.ASSEMBLY_LOCATION)
		AssembleBuilding()



