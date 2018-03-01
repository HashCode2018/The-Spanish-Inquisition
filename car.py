class Car:
    def __init__(self, ID):
        self.a = 0
        self.b = 0
        self.busy = False
        self.current_ride = None
        self.history = []
        self.ID = ID