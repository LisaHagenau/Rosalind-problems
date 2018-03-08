from __future__ import division
# number of individuals
pop =[30,17,19]
total = sum(pop)
total2 = total-1
print total, total2

# probability of individuals mating based on their number
p0 = [i/total for i in pop]

# first draw from population
p1 = [x for x in p0 for i in range(len(pop))]

# second draw from population
p2 = [(pop[0]-1)/total2, pop[1]/total2, pop[2]/total2, pop[0]/total2, (pop[1]-1)/total2, pop[2]/total2, pop[0]/total2, pop[1]/total2, (pop[2]-1)/total2]

# probabilities for dominant alleles between any type of individual
p3 = [1,1,1,1,0.75,0.5,1,0.5,0]

# probability for dominant alleles in random pairing
comb = [p1[i]*p2[i]*p3[i] for i in range(len(p1))]
print sum(comb)