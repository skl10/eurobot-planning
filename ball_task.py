from planner import get_time


def navigate_to(location):
#	go to location
#	(this finishes executing when robot has arrived at goal location)

def open_latch():
#	open the latch in front of us -- make adjustments to pose as necessary

def collect_balls():
#	get balls from recuperator and categorise them

def deposit_balls():
#   navigate to appropriate tower
#   deposit balls

our_tower = True
# our_tower: boolean value that keeps track of whether
# we’re going to our tower or not (makes it easier to generalise
# code while navigating, and enables us to know which
# colour balls we should deposit)

#
# ADD CHECKS FOR NEARBY RESOURCES
# also add something that publishes when task has been completed
#

max_time = 1000 # placeholder: how long can we do this task for?

start_time = get_time()


while (get_time() - start_time) < max_time:

# THIS DEPENDS ON HOW BALL COLLECTION, SORTING, DEPOSITING ENDS UP HAPPENING

	navigate_to(first_recup_location)
	# I will assume that navigate_to stops executing only once we arrive
	# at our chosen location

	open_latch()

	collect_balls()

	# if we have capacity for more balls, go to more recuperators? or drop off
	# on the way? depends on locations

	navigate_to(second_recup_location)

	open_latch()

	collect_balls()


	if(dist_to_our_tower <= dist_to_their_tower):
	# [note: any reason to choose one over the other if distance is equal?]
		our_tower = True # keeps track of which tower we're at
		navigate_to(our_tower_location)
		deposit_balls(our_tower)

		navigate_to(their_tower_location)
		our_tower = False
		deposit_balls(our_tower)

	else if (dist_to_their_tower < dist_to_our_tower):
		our_tower = False
		navigate_to(their_tower_location)
		deposit_balls(our_tower)

		navigate_to(our_tower_location)
		our_tower = True
		deposit_balls(our_tower)

