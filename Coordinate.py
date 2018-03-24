class Coordinate:

    def __init__(self, x, y, z=0):
        self.x = x
        self.y = y
        self.z = z

    def GetCoordinates(self):
        return [self.x, self.y, self.z]
