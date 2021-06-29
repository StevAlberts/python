"""Define Agent Parameters"""

loc = ['1','2','3','4']
move = ['U','D','L','R']
path = {
    "1R":"2", "1D":"3","2L":"1","2D":"4",
    "3R":"4", "3U":"1","4L":"3","4U":"2",
    "1U":"W", "1L":"W","2U":"W","2R":"W",
    "3D":"W", "2L":"W","4R":"W","4D":"W"
}

""" Create Agent """
def make_agent(loc):
    return [loc]

"""Make Agent Move"""
import random
def choose_path(agent_one):
    i = random.choice(move)
    j = str(agent_one[0])+i
    print("printng direction to move ... ",i)
    print("printing j...agents new position ",j)
    print("printing path j...destionation ",path[j])

    while path[j] == "W":
        i = random.choice(move)
        j = str(agent_one[0])+i
        print("printng direction to move ... ",i)
        print("printing j...agents new position ",j)
        print("printing path j...destionation ",path[j])
        print("cant move ",i)

    print("path chosen ",path[j])
    return j

"""Agent Takes Journey"""
journey=[]
def take_journey():
    agent_one = make_agent(random.choice(loc))
    print("Agent Loc: ",agent_one)
    journey.append(agent_one[0])
    while agent_one[0] != '4':
        to_move=choose_path(agent_one)
        agent_one[0] = path[to_move]
        print("moved to loc ",agent_one[0])
        journey.append(agent_one[0])
    journey.append(4)
    print("journey ",journey)
take_journey()

"""Visualize journey"""

import matplotlib.pyplot as plt
plt.title('Agent Journey over time')
plt.ylabel('Agent Location')
plt.xlabel('Time')
plt.plot(journey)
plt.show()
