import random


class Environment(object):
    def __init__(self):
        # instantiate locations and conditions
        # 0 indicates  Clean and 1 indicates Dirty
        self.Location = ['A','B','C','D']
        self.locationCondition = {'A': '0', 'B': '0','C': '0','D': '0'}

        self.cleaningMethod = {'A':'L','B':'T','C':'L','D':'T'}


class SimpleReflexVacuumAgent(Environment):
    def __init__(self, Environment):
        Environment.locationCondition['A'] = random.randint(0,1)
        Environment.locationCondition['B'] = random.randint(0,1)
        Environment.locationCondition['C'] = random.randint(0,1)
        Environment.locationCondition['D'] = random.randint(0,1)

        print (Environment.locationCondition)
        print (Environment.cleaningMethod)

        Score = 0

        vacuumLocation = random.choice(Environment.Location)

        print("Vacuum is randomly placed at Location.", vacuumLocation)

        count = 0

        while count <4:
            print("test", Environment.locationCondition[vacuumLocation])
            if Environment.locationCondition[vacuumLocation] == 1:
                print(vacuumLocation, " is Dirty.")
                if Environment.cleaningMethod[vacuumLocation] == 'T':
                    Environment.cleaningMethod[vacuumLocation] = 'L'
                else :
                    Environment.cleaningMethod[vacuumLocation] = 'T'
                Environment.locationCondition[vacuumLocation] = 0
                print(vacuumLocation, " has been Cleaned.")
            else:
                print(vacuumLocation, " is Clean.")
            newIndex = Environment.Location.index(vacuumLocation) + 1

            if newIndex == 4:
                newIndex = 0
            vacuumLocation = Environment.Location[newIndex]
            count+=1

        print(Environment.locationCondition)

theEnvironment = Environment()
for i in range(2):
    theVacuum = SimpleReflexVacuumAgent(theEnvironment)


    
