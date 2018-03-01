class Ride:

    def __init__(self, a, b, x, y, s, f, ID):
        self.a = a
        self.b = b
        self.x = x
        self.y = y
        self.s = s
        self.f = f
        self.distance = abs(a-x) + abs(b-y)
        self.ID = ID

