from car import Car
from ride import Ride

class Parser:

    def __init__(self):
        pass

    @staticmethod
    def ParseInput(f):
        p = [list(map(int, line.split(" "))) for line in open("./data/" + f).read().split("\n") if line.__len__()!=0]
        
        R = p[0][0]
        C = p[0][1]
        B = p[0][4]
        T = p[0][5]

        F = [Car(i) for i in range(p[0][2])]
        N = [Ride(r[0], r[1], r[2], r[3], r[4], r[5], i-1) for i,r in enumerate(p) if i>0]

        N.sort(key=lambda x: x.f, reverse=True)

        return R, C, F, N, B, T

p = Parser()

r,c,f,n,b,t = p.ParseInput("a_example.in")

for x in n:
    print(x.f)