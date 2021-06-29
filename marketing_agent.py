"""CREATE AN AGENT ENVIRONMENT"""
"""Define Agent Parameters"""
data = ['a', 'i']
personalities = ['F', 'S'] 
print (data[1])

"""Create Agent"""
def make_agent(data, personality):                      #write Agent function
    return [data, personality]

agent_one = make_agent(data[1], personalities[0])       #call function
print ("Agent: ", agent_one )                           #print results

"""Create Identical Population"""
def make_population_identical(N):                       #write Population function
    population = [] 
    for i in range(N):
          agent = make_agent(data[1], personalities[0]) 
          population.append(agent)
    return population

population_test = make_population_identical(5)          #call function
print ("Identical Population: ",population_test)                  #print results

"""Create Random Population"""
import random
def make_population_random(N):                                      #write random Population function
    population = []
    for i in range(N):
                d = random.choice(data)
                p = random.choice(personalities)
                agent = make_agent(d, p)
                population.append(agent)
    return population

def count(population):                                              #Describe population
    t = 0.0 # to make it a float!     
    for agent in population:
        if agent[0] == 'a':
            t = t+1            
    return t / len(population) 

prop_a = count(make_population_random(20))                          #Create & Describe random population
print ("Random Population: ",make_population_random(20))                  #print results
print ('The proportion of [a] in the population is', prop_a)

"""MAKE AGENTS INTERACT"""
"""Select Random Agent"""
from numpy.random import choice

def choose_pair(population):
    i = random.randint(0, len(population) - 1)                              #pick 2 random ajents (i,j) between 0 and n-1
    j = random.randint(0, len(population) - 1) 
    while i == j:
        j = random.randint(0, len(population) - 1)#change if same agent 
    return population[i], population[j]

listener, producer = choose_pair(make_population_random(20))
print ('The population is', make_population_random(20)) 
print ('This is the chosen pair', listener, producer )
print ('The listener is', listener )
print ('The producer is', producer)

"""Make Agent Interact"""
from copy import deepcopy
def interact_test(listener, producer): 
    if listener[0] == producer[0]:#exit if are agent similar
        return listener 
    else:
        if listener[1]=='S': #exit if are agent stubborn
            return listener 
        else:
            listener[0]=deepcopy(producer[0])
    return listener #omit this when running the simulation

updated_listener = interact_test(listener, producer)
print ('After interacting, the listener is',updated_listener)



"""SIMULATE REPEATED INTERACTIONS"""
"""Interact without returning values"""
def interact(listener,producer): 
    if listener[0] == producer[0]:
        pass    # do nothing
    else:
        if listener[1]=='S':
            pass
        else:
            listener[0]=deepcopy(producer[0])

"""Interact n agents k times"""
def simulate(n, k):
    population = make_population_random(n)
    proportion = []     # create list to store proportions after every interaction
    for i in range(k):  # call interact k times
        pair = choose_pair(population) # choose a pair from the population
        listener, producer = choose_pair(population)
        interact(listener, producer)  # make the chosen pair interact
        proportion.append(count(population)) # store proportion in list
    return population, proportion

population, proportion = simulate(20, 500) # Simulate 500 interactions between 20 agents 
print ("Population after 500  interactions:", population)

"""Visualize population change after k interactions"""
import matplotlib.pyplot as plt # importing a plotting library
plt.title('Changes in the proportion of [a] over time') # and add some details to the plot
plt.ylabel('Proportion [a] users')
plt.xlabel('Time [No. of interactions]')
plt.plot(proportion)
plt.show()

"""Increase agents and interactions""" 
population, proportion = simulate(200, 5000)
#print "Final Population:", population
plt.plot(proportion)
plt.show()
"""Simulate iterations 20 times""" 
def batch_simulate(n,k,s):
    batch_proportions=[]
    for i in range(s):
        population, proportion = simulate(n, k)
        batch_proportions.append(proportion)

results = batch_simulate(200,5000,20)
for i in results:
    plt.plot(i)
    plt.show()