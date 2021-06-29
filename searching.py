"""The Environment"""
class Environment(object):
    graph = {
        "1":set(["2","3"]),
        "2":set(["1","4"]),
        "3":set(["1","4"]),
        "4":set(["2","3"])
    }

    goal = "1"
    state = "2"

"""Agent Behaviour"""
#Depth first search

class Agent(Environment):
    def dfs(graph, start, goal):
        stack = [(start, [start])]
        p = []
        while stack:
            (vertex, path) = stack.pop()
            for next in graph[vertex] - set(path):
                if next == goal:
                    p.append(path + [next])
                else:
                    stack.append((next, path + [next]))

        return p

    #Breath First Search
    def bfs(graph, start, goal):
        queue = [(start, [start])]
        p = []
        while queue :
            (vertex, path) = queue.pop(0)
            #poping 0 make it a queue
            for next in graph[vertex] - set(path):
                if next == goal:
                    p.append(path + [next])
                    return p
                    #first path returned by bfs is the shortest path
                    #we dont need to check the rest
                else:
                    queue.append((next, path + [next]))
        return p

    def __init__(self, Environment):
        print("DFS-Paths Available")
        print(Agent.dfs(Environment.mygraph, Environment.Goal, Environment.State))
        #returns all possible routes
        print("BFS-Shortest Path")
        print(Agent.bfs(Environment.mygraph, Environment.Goal, Environment.State))
        #returns shortest routes

"""Create the agent"""
theEnvironment = Environment()
theAgent = Agent(theEnvironment)
