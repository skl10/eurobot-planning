from Coordinate import Coordinate

class Tower:
    def __init__(self, x, y, z=0):
        self.position = Coordinate(x, y, z)

TOTAL_TASKS = 4
INIT_BALL_LIMIT = 100
INIT_BLOCK_LIMIT = 100
INIT_FLOWER_LIMIT = 100
INIT_SWITCH_LIMIT = 100

# Important Locations
first_recup_location = Coordinate(0, 0, 0) # placeholder
second_recup_location = Coordinate(1, 1, 1) # placeholder

our_tower = Tower(2, 2, 2) # placeholder
their_tower = Tower(2, 2, 2) # placeholder
