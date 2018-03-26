from planner import get_time


def navigateTo(location):
#	go to location
#	(this finishes executing when robot has arrived at goal location)

def openLatch():
#	open the latch in front of us -- make adjustments to pose as necessary

def collectBalls():
#	get balls from recuperator and categorise them

def depositBalls():
#   navigate to appropriate tower
#   deposit balls

ourTower = True
# our_tower: boolean value that keeps track of whether
# we’re going to our tower or not (makes it easier to generalise
# code while navigating, and enables us to know which
# colour balls we should deposit)

#
# ADD CHECKS FOR NEARBY RESOURCES
# also add something that publishes when task has been completed
#

maxTime = 1000 # placeholder: how long can we do this task for?

startTime = getTime()

while (getTime() - startTime) < maxTime:

# THIS DEPENDS ON HOW BALL COLLECTION, SORTING, DEPOSITING ENDS UP HAPPENING

	navigateTo(firstRecupLocation)
	# I will assume that navigate_to stops executing only once we arrive
	# at our chosen location

	openLatch()

	collectBalls()

	# if we have capacity for more balls, go to more recuperators? or drop off
	# on the way? depends on locations

	navigateTo(secondRecupLocation)

	openLatch()

	collectBalls()


	if(distToOurTower <= distToTheirTower):
	# [note: any reason to choose one over the other if distance is equal?]
		ourTower = True # keeps track of which tower we're at
		navigateTo(ourTowerLocation)
		depositBalls(ourTower)

		navigateTo(theirTowerLocation)
		ourTower = False
		depositBalls(ourTower)

	else if (distToTheirTower < distToOurTower):
		ourTower = False
		navigateTo(theirTowerLocation)
		depositBalls(ourTower)

		navigateTo(ourTowerLocation)
		ourTower = True
		depositBalls(ourTower)

