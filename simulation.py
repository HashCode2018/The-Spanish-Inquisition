from ride import Ride
from car import Car
from parser import Parser


class Simulation:

    def __init__(self, filename):
        self.R, self.C, self.cars, self.rides, self.B, self.T = Parser.ParseInput(filename)
        self.F = len(self.cars)
        self.N = len(self.rides)

    def exec(self):
        for t in range(self.T):
            # Find a car for a ride
            if len(self.rides) == 0:
                break
            for ride in self.rides:
                car = find_my_car(ride)
                car.start(ride)
                self.rides.remove(ride)
            for car in self.cars:
                car.simulation_step()


    def get_distance(self, car, ride):
        return abs(car.a-ride.a)+abs(car.b-ride.b)

    def find_my_car(self, ride):
        distances = []
        res = None
        MinDist = self.R + self.C

        MinTimeToFinal = ride.f - self.t

        car_index = 0


        for i,car in enumerate(self.cars):

            if car.busy:
                continue

            dist = self.get_distance(car,ride)

            if (dist + ride.distance) > MinTimeToFinal:
                continue

            if MinDist > dist:
                car_index = i
                MinDist = dist



        return self.cars[car_index]



