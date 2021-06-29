import operator
"""The Environment"""
class Environment(object):
    mygraph = { "1" : set(["2", "5"]),
                "2" : set(["1", "3", "6"]),
                "3" : set(["2", "7","4"]),
                "4" : set(["3", "8"]),
                "5" : set(["1", "6", "9"]),
                "6" : set(["2", "5", "10"]),
                "7" : set(["3", "6","8","11"]),
                "8" : set(["4", "7", "12"]),
                "9" : set(["5", "10","13"]),
                "10" : set(["6", "9","11","12"]),
                "11" : set(["7", "10","12","15"]),
                "12" : set(["8", "11","16"]),
                "13" : set(["9", "14"]),
                "14" : set(["10", "13","15"]),
                "15" : set(["11", "14","16"]),
                "16" : set(["12", "15"]),
 } 
    myheuristics= { "1" : ["1", "4"],
                    "2" : ["2", "4"],
                    "3" : ["3", "4"],
                    "4" : ["4", "4"],
                    "5" : ["1", "3"],
                    "6" : ["2", "3"],
                    "7" : ["3", "3"],
                    "8" :["4", "3"],
                    "9" : ["1", "2"],
                    "10" : ["2", "2"],
                    "11" : ["3", "2"],
                    "12" : ["4", "2"],
                    "13" : ["1", "1"],
                    "14" : ["2", "1"],
                    "15" : ["3", "1"],
                    "16" : ["4", "1"]
                } 
    # myheuristics - manhattan distance
    # cost- Distance between two nodes(sum of the nodes)
 
    Goal="8"
    State="1"

"""Agent Behaviour"""
#Depth First Search
class Agent(Environment):

#Calculate Heuristics
# myheuristics - manhattan distance
 def getheur(vertex, goal):
     v=[]
     g=[]
     for i in Environment.myheuristics[vertex]:
        v.append(int(i))
     for i in Environment.myheuristics[goal]:
        g.append(int(i))   
     heuristic = abs(v[0]-g[0])+abs(v[1]-g[1])
     return heuristic
 #calculate cost
# cost- Distance between two nodes(sum of the nodes)
 
 def getcost(vertex, neighbour):
        cost = int(vertex)+int(neighbour)
        return cost
       

 def getheur(vertex, goal):
        v=[]
        g=[]
        for i in Environment.myheuristics[vertex]:
            v.append(int(i))
        for i in Environment.myheuristics[goal]:
            g.append(int(i))
        heuristics = abs(v[0]-g[0])+abs(v[1]-g[1])
        return heuristics

 def A_Star(graph,start, goal):
    p=[]
    p.append(start)
    while True:
        neighbour = graph[start]
        heur={}
        for i in neighbour.difference(p):
            heur[i] = Agent.getheur(i,goal)+Agent.getcost(start,i)
        sorted_heur = sorted(heur.items(), key=operator.itemgetter(1))
        x=next(iter(sorted_heur[0]))
        p.append(x)
        if x == goal:
            return p 
        else:
            start=x

  

 def __init__(self, Environment):
 

   
    
    print("A_Star-Paths Available")
    print(Agent.A_Star(Environment.mygraph,Environment.Goal, Environment.State)) 
    # returns all possible routes

"""Create the agent"""
theEnvironment = Environment()
theAgent= Agent(theEnvironment)