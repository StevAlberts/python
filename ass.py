import random


class Environment(object):
    def __init__(self):
        # instantiate locations and conditions
        # 0 indicates Clean and 1 indicates Dirty

        self.locationCondition = {'A': '0', 'B': '0'}
        self.cleaning_history = {'A':'T' , 'B':'T'}

        # randomize conditions in locations A and B
        self.cleaning_history['A'] = random.random(T,L)
        self.cleaning_history['B'] = random.random(T,L)
        self.locationCondition['A'] = random.randint(0, 1)
        self.locationCondition['B'] = random.randint(0, 1)

        self.history = [] #memory of the type of cleaning

class SimpleReflexVacuumAgent(Environment):
    def __init__(self, Environment):
        print (Environment.locationCondition)
        # Instantiate performance measurement
        Score = 0
        # place vacuum at random location
        vacuumLocation = random.randint(0, 1)
        # if vacuum at A
        if vacuumLocation == 0:
            print ("Vacuum is randomly placed at Location A.")
            # and Location A is Dirty.
            if Environment.locationCondition['A'] == 1:
                print ("Location A is Dirty.")
                if Environment.cleaning_history == 'L':
                    # suck the dirt  and mark it clean
                    Environment.locationCondition['A'] = 0;
                    print ("Location A has been thoroughly cleaned.")
                    Environment.cleaning_history == 'T'
                else:
                    Environment.cleaning_history == 'T'
                    Environment.locationCondition['A'] = 0;
                    print ("Location A has been lightly cleaned.")
                    Environment.cleaning_history == 'L'
            # move to B
            print ("Moving to Location B...")
             # if B is Dirty
            if Environment.locationCondition['B'] == 1:
                print ("Location B is Dirty.")
                if Environment.cleaning_history == 'L':
                    # suck and mark clean
                    Environment.locationCondition['B'] = 0;
                    print ("Location B has been thoroughly cleaned.")
                    Environment.cleaning_history == 'T'
                else:
                    Environment.cleaning_history == 'T'
                    Environment.locationCondition['B'] = 0;
                    print ("Location A has been lightly cleaned.") 
                    Environment.cleaning_history == 'L'
            else:
                # move to B
                
                print ("Moving to Location B...")
                # if B is Dirty
                if Environment.locationCondition['B'] == 1:
                    print ("Location B is Dirty.")
                    if Environment.cleaning_history == 'L':
                        # suck and mark clean
                        Environment.locationCondition['B'] = 0;
                        print ("Location B has been thorougly cleaned.") 
                        Environment.cleaning_history == 'T'
                    else:
                        Environment.cleaning_history == 'T'
                        Environment.locationCondition['B'] = 0;
                        print ("Location A has been lightly cleaned.")
                        Environment.cleaning_history == 'L'

        elif vacuumLocation == 1:
            print ("Vacuum randomly placed at Location B.")
            # and B is Dirty
            if Environment.locationCondition['B'] == 1:
                print ("Location B is Dirty.")
                if Environment.cleaning_history == 'L':
                    # suck and mark clean
                    Environment.locationCondition['B'] = 0;
                    print ("Location B has been thorougly cleaned.")
                    Environment.cleaning_history == 'T'
                else:
                    Environment.cleaning_history == 'T'
                    Environment.locationCondition['B'] = 0;
                    print ("Location A has been lightly cleaned.")
                    Environment.cleaning_history == 'L'
               
                # move to A
                print ("Moving to Location A...")
                # if A is Dirty
                if Environment.locationCondition['A'] == 1:
                    print ("Location A is Dirty.")
                    if Environment.cleaning_history == 'L':
                        # suck and mark clean
                        Environment.locationCondition['A'] = 0
                        print ("Location A has been thorougly cleaned.")
                        Environment.cleaning_history == 'T'
                    else:
                        Environment.cleaning_history == 'T'
                        Environment.locationCondition['A'] = 0;
                        print ("Location A has been lightly cleaned.")
                        Environment.cleaning_history == 'L'
            else:
                # move to A
                print ("Moving to Location A...")
                # if A is Dirty
                if Environment.locationCondition['A'] == 1:
                    print ("Location A is Dirty.")
                    if Environment.cleaning_history == 'L':
                        # suck and mark clean
                        Environment.locationCondition['A'] = 0;
                        print ("Location A has been thorougly cleaned.")
                        Environment.cleaning_history == 'T'
                    else:
                        Environment.cleaning_history == 'T'
                        Environment.locationCondition['A'] = 0;
                        print ("Location A has been lightly cleaned.")
                        Environment.cleaning_history == 'L'
        # done cleaning
        print (Environment.locationCondition)
        

for i in range(20):
    theEnvironment = Environment()
    theVacuum = SimpleReflexVacuumAgent(theEnvironment)

