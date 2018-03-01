from ride import Ride

class Car:


    def __init__(self, ID):
        self.a = 0
        self.b = 0
        self.busy = False
        self.current_ride = None
        self.history = []
        self.ID = ID
        self.time_to_stop = 0

    def start(self, ride):
        history.append(ride.ID)
        self.time_to_stop = ride.distance
        self.busy = True
        a = ride.x
        b = ride.y

    def simulation_step(self):
        if time_to_stop > 0:
            self.time_to_stop += -1
        else:
            self.busy = False
