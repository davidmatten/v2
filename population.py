
import random
from node import node

class population:

    population = None
    households = None

    def __init__(self, n=10):
        self.population = [node() for x in range(n)]

    def __repr__(self):
        for n in self.population:
            print n 
        return ""
    
    def set_infection(self, prevelance=30):
        for p in self.population:
            r = random.randint(0, 100)
            if r < prevelance:
                p.status = True
            else:
                p.status = False

    def get_size(self):
        return len(self.population)

    def set_housing(self):
        self.households = {}
        i, h = 0, 0
        for p in self.population:
            r = random.randint(1,3)
            print "A new household: "
            print self.population[i:i+r]
            h += 1
            self.households[h] = self.population[i:i+r]
            i += r
            if i > len(self.population):
                break
            print "finished making houses"

