class Task(Enum):
	WATER = 1
	BUILDINGS = 2
	FLOWER = 3
	SWITCH = 4

class Tower:
	def __init__(self, x, y, z=0):
		self.position = Coordinate(x, y, z)

first_recup_location = Coordinate(0, 0, 0) # placeholder
second_recup_location = Coordinate(1, 1, 1) # placeholder

our_tower = Tower(2, 2, 2) # placeholder
their_tower = Tower(2, 2, 2) # placeholder
