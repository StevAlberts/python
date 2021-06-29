
import random

# Instantiate performance measurement
V1_Score = []
V2_Score = []

class Environment(object):
    def __init__(self):
        # instantiate locations and conditions
        # 0 indicates Clean and 1 indicates Dirty
        self.Location=['A','B','C','D']
        self.locationCondition = {'A': '0', 'B': '0','C': '0', 'D': '0'}

        #Cleaning Record [T=thorough, L=Light]
        #Assume past record is 'A'= 'L' and 'B'= 'T'
        self.cleaningMethod = {'A': 'L', 'B': 'T','C': 'L', 'D': 'T',}
        
        #Location Status [Y=Visited, N=Not Visited]
        self.Visited = {'A': 'N', 'B': 'N','C': 'N', 'D': 'N',}

        # place vacuums at different random locations
        self.vacuumLocation1 = random.choice(self.Location)
        self.vacuumLocation2 = random.choice(self.Location)
        while self.vacuumLocation1 == self.vacuumLocation2: 
            self.vacuumLocation2 = random.choice(self.Location)
        print ("Vacuums are randomly placed at Location.", self.vacuumLocation1,self.vacuumLocation2)
        self.Visited[self.vacuumLocation1]='Y' #Mark Locations a visited
        self.Visited[self.vacuumLocation2]='Y'
        print(self.Visited)

        # randomize conditions 
        self.locationCondition['A'] = random.randint(0, 1)
        self.locationCondition['B'] = random.randint(0, 1)
        self.locationCondition['C'] = random.randint(0, 1)
        self.locationCondition['D'] = random.randint(0, 1)

        print (self.locationCondition)
        print (self.cleaningMethod)


class SimpleReflexVacuumAgent(Environment):
   def __init__(self, Environment,agentNo):
        
        # Instantiate performance measurement
        performance = 0
                         
        
        # and Location is Dirty.
        if agentNo=='i':
            if Environment.locationCondition[Environment.vacuumLocation1] == 1 :
                print (Environment.vacuumLocation1," is Dirty.")
                # check state, suck, mark clean, record state
                if Environment.cleaningMethod[Environment.vacuumLocation1] == 'T':
                    Environment.cleaningMethod[Environment.vacuumLocation1] = 'L'
                else:
                    Environment.cleaningMethod[Environment.vacuumLocation1] = 'T'
                Environment.locationCondition[Environment.vacuumLocation1] = 0;
                print (Environment.vacuumLocation1,"has been Cleaned.")
                V1_Score.append(1) 
            else:
                print (Environment.vacuumLocation1," is Clean.")
             
            #Move agent to non-visited location
            count=0
            newIndex=Environment.Location.index(Environment.vacuumLocation1)
            while True:  #emulate do while loop
                newIndex=newIndex+1
                print("Vacuum 1 Old and New Index",Environment.Location.index(Environment.vacuumLocation1),newIndex)
                if newIndex == 4:
                    newIndex=0
                Environment.vacuumLocation1=Environment.Location[newIndex] 
                print("Vacuum 1 New Location and Status",Environment.vacuumLocation1,Environment.Visited[Environment.vacuumLocation1])
                count+=1
                if   Environment.Visited[Environment.vacuumLocation1] =='N':
                    Environment.Visited[Environment.vacuumLocation1]='Y' #Mark new Locations a visited
                    print("Vacuum 1 moved vacuum to location",Environment.vacuumLocation1)
                    break 
                elif count==4:
                    print("Vacuum 1 Exiting...All Locations Cleaned!")
                    break 
        else:
            if Environment.locationCondition[Environment.vacuumLocation2] == 1 :
                print (Environment.vacuumLocation2," is Dirty.")
                # check state, suck, mark clean, record state
                if Environment.cleaningMethod[Environment.vacuumLocation2] == 'T':
                    Environment.cleaningMethod[Environment.vacuumLocation2] = 'L'
                else:
                    Environment.cleaningMethod[Environment.vacuumLocation2] = 'T'
                Environment.locationCondition[Environment.vacuumLocation2] = 0;
                print (Environment.vacuumLocation2,"has been Cleaned.")
                V2_Score.append(1) 
            else:
                print (Environment.vacuumLocation2," is Clean.")
             
            #Move agent to non-visited location
            count=0
            newIndex=Environment.Location.index(Environment.vacuumLocation1)
            while True:  #emulate do while loop
                newIndex=newIndex+1
                print("Vacuum 2 Old and New Index",Environment.Location.index(Environment.vacuumLocation2),newIndex)
                if newIndex == 4:
                    newIndex=0
                Environment.vacuumLocation2=Environment.Location[newIndex]  
                print("Vacuum 2 New Location and Status",Environment.vacuumLocation2,Environment.Visited[Environment.vacuumLocation2])
                count+=1
                if   Environment.Visited[Environment.vacuumLocation2] =='N':
                    Environment.Visited[Environment.vacuumLocation2]='Y' #Mark new Locations a visited
                    print("moved vacuum to location",Environment.vacuumLocation2)
                    break 
                elif count==4:
                    print("Vacuum 2 Exiting...All Locations Cleaned!")
                    break 
        print(Environment.Visited)

for i in range(20): #run N tests to see how each agent performed
    theEnvironment = Environment()
    for i in range(2):
        theVacuum_i = SimpleReflexVacuumAgent(theEnvironment,'i')
        theVacuum_j = SimpleReflexVacuumAgent(theEnvironment,'j')


print("V1_Score",V1_Score,'=',(sum(V1_Score)/(sum(V1_Score)+sum(V2_Score)))*100,'%')
print("V2_Score",V2_Score,'=',(sum(V2_Score)/(sum(V1_Score)+sum(V2_Score)))*100,'%')
