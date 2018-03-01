class Ride:
    a = None
    b = None
    x = None
    y = None
    s = None
    f = None
    completed = False
    distance = None

    def __init__(self, a, b, x, y, s, f, ID):
        self.a = a
        self.b = b
        self.x = x
        self.y = y
        self.s = s
        self.f = f
        self.distance = abs(a-x) + abs(b-y)
        self.id = ID

