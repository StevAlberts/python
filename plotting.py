import os
import random

performance = []

class Environment(object):
    def __init__(self):
        self.filelist=[]
        path = "/Users/mac/development/cleaned"
        for i in os.listdir(path):
            self.filelist.append(i)
            print(i)

        self.agentfind = random.randint(0, len(self.filelist) - 1)
        print("Searching for ", self.filelist[self.agentfind])

class Agent(Environment):
    def __init__(self, Environment):
        count  = 0
        for i in Environment.filelist:
            if i == Environment.filelist[Environment.agentfind]:
                print("File foind in location: ",count)
                performance.append(count)
            else:
                count=count+1

for x in range(0,20):
    theEnvironment = Environment()
    theAgent = Agent(theEnvironment)

print("performance ", performance)
print("Average search time ", sum(performance)/len(performance))

# import matplotlib.pyplot as plt

# plt.title('Agent Journey iver time')
# plt.ylabel('Agent Location')
# plt.xlabel('Time')
# plt.plot(performance)
# plt.show()