from ride import Ride
from car import Car
from xparser import xParser

class Simulation:

    def __init__(self, filename):

        self.R, self.C, self.cars, self.rides, self.B, self.T = xParser.ParseInput(filename)
        self.F = len(self.cars)
        self.N = len(self.rides)
        self.t = 0
        self.T100 = self.T/100
        self.nextStage = 0


    def xexec(self):
        maxCars = 100
        firstCar = 0
        self.T = 100
        for t in range(self.T):
            if t > 2000:
                break
            if t > self.nextStage:
                self.nextStage += self.T100
                print(str(t)+" from "+str(self.T))


            self.t = t
            # Find a car for a ride
            if len(self.rides) == 0:
                break
            for ride in self.rides:
                car = self.find_my_car(ride, firstCar, maxCars)
                firstCar += maxCars
                if firstCar >= len(self.cars)-maxCars:
                    firstCar = 0
                if car == None:
                    continue

                car.start(ride)
                self.rides.remove(ride)
            for car in self.cars:
                car.simulation_step()

        xParser.ParseOutput(self.cars)


    def get_distance(self, car, ride):
        return abs(car.a-ride.a)+abs(car.b-ride.b)

    def find_my_car(self, ride, firstCar, maxCars):
        MinDist = self.R + self.C

        MinTimeToFinal = ride.f - self.t

        car_index = None


        for i,car in enumerate(self.cars):
        #for i in range(firstCar, firstCar+maxCars):

            if car.busy:
                continue

            dist = self.get_distance(car,ride)

            if (dist + ride.distance) > MinTimeToFinal:
                continue

            if MinDist > dist:
                car_index = i
                MinDist = dist


        if car_index == None:
            return None
        return self.cars[car_index]


s = Simulation("e_high_bonus.in")
s.xexec()