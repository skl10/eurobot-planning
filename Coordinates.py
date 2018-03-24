class Coordinate:

    def __init__(self, x, y, z=0):
        # Defualt z value is zero as it's assumed most objects
        # will be on the ground
        self.x = x
        self.y = y
        self.z = z

    def GetCoordinates(self):
        return [self.x, self.y, self.z]
