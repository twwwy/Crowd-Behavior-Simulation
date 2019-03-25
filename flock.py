from setting import *

class Flock(object):
    
    def __init__(self):
        self.vehicle = []
        
    def run(self, target=PVector(500, 500), color_int=127):
        for b in self.vehicle:
            b.run(self.vehicle, target, color_int)
    
    def addBoid(self, b):
        self.vehicle.append(b)
        boids.append(b)
        
