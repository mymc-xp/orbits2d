#graphing gravitation along a 2d plane, setting earth to be stationary
#G = 6.67430*10^-11 N*m^2/kg^2 gravity constant
#moon mass 7.34767309 × 10^22
#earth mass 5.972 × 10^24 kg
#F = G*m1m2/r^2 gravity times product of masses over distance squared
import math
import matplotlib.pyplot as plt 
class body:
    def __init__(self, mass = 1, coords = (0,0), velocity = (0,0)): #kg, location, 
        self.mass = mass
        self.coords = coords
        self.velocity = velocity
    def add_velocity(self, velocity):
        self.velocity = (self.velocity[0] + velocity[0], self.velocity[1] + velocity[1])
    def travel(self, s):
        self.coords = (self.coords[0] + self.velocity[0]*s, self.coords[1] + self.velocity[1]*s)
    def distance_from(self, other):
        x = self.coords[0] - other.coords[0]
        y = self.coords[1] - other.coords[1]
        return (x**2 + y**2)**(1/2)
moon = body(7.34767309 * 10**22, (0, 384400000), (1,0))#moon apparently travels 102200 m/s n
earth = body(597.2, (0,0), (0,0))
l = []
x = [0, 0]
y = [0, 384400000]
for s in range(1000000):
    force = ((6.67430*(10**-11))*moon.mass*earth.mass)/(moon.distance_from(earth)**2)
    xc = -1 if moon.coords[0] > earth.coords[0] else 1
    yc = -1 if moon.coords[1] > earth.coords[1] else 1
    if moon.coords[0] == 0:
        angle = math.pi / 2
    elif moon.coords[1] == 0:
        angle = 0
    else:
        angle = math.atan(moon.coords[1]/moon.coords[0])
    xforce = force*math.cos(angle)
    yforce = force*math.sin(angle)
    xaccel = xforce / moon.mass 
    yaccel = yforce / moon.mass
    moon.add_velocity((xc*xaccel,yc*yaccel))
    moon.travel(1)
    l.append(s)
    x.append(moon.coords[0])
    y.append(moon.coords[1])
plt.scatter(x, y)
plt.show()
    