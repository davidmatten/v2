
from node import node
import random
from population import population

## Group population into houses, between 1 and 6 members per house-hold. #TODO: Can find the real values (mean household size, variance) from the Census.
#households = {}
#i, h = 0, 0
#for p in population:
#    r = random.randint(1,3)
#    print "A new household: "
#    print population[i:i+r]
#    h += 1
#    households[h] = population[i:i+r]
#    i += r
#    if i > len(population):
#        break
#print "finished making houses"


p = population()
print "established population of %s." %p.get_size()
p.set_infection(40)
print "set infections"

p.set_housing()
print "housed the population"

alice = p[0]
bob = p[1]
p.create_relationship(alice, bob)
print "created a relationship between alice and bob"

print p.get_relationships()


print p
