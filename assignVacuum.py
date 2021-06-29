import random

class Environment(object):
    def __init__(self):
        self.locationCondition = {'A':'0', 'B':'0'}

        self.locationCondition['A'] = random.randint(0,1)
        self.locationCondition['B'] = random.randint(0,1)

class LightVacuumAgent(Environment):
    def __init__(self,Environment):
        print(Environment.locationCondition)
        Score = 0
        vacuumLocation = random.randint(0,1)

        if vacuumLocation == 0:
            print("Vacuum is randomly placed at Location A.")
            
            if Environment.locationCondition['A'] == 1:
              print("Location A is Dirty.")
              Environment.locationCondition['A'] = 0
              print("Location A has been changed. ")
              print("Moving to Location B...")

              if Environment.locationCondition['B'] == 1:
                  print("Location B is dirty. ")
                  Environment.locationCondition['B'] = 0
                  print("Location B has been Cleaned. ")

            else:
                print("Moving to Location B...")
                if Environment.locationCondition['B'] == 1:
                    print("Location B is dirty. ")
                    Environment.locationCondition['B'] = 0
                print("Location B has been Cleaned.")

        elif vacuumLocation == 1:
            print("Vacuum is randomly placed at Location B.")
            
            if Environment.locationCondition['B'] == 1:
              print("Location B is Dirty.")
              Environment.locationCondition['B'] = 0
              print("Location B has been changed. ")
              print("Moving to Location A...")

              if Environment.locationCondition['A'] == 1:
                  print("Location A is dirty. ")
                  Environment.locationCondition['B'] = 0
                  print("Location A has been Cleaned. ")

            else:
                print("Moving to Location A...")
                if Environment.locationCondition['A'] == 1:
                    print("Location A is dirty. ")
                    Environment.locationCondition['A'] = 0
                print("Location A has been Cleaned.")

        print(Environment.locationCondition)


class ThoroughVacuumAgent(Environment):
    def __init__(self,Environment):
        print(Environment.locationCondition)
        Score = 1
        vacuumLocation = random.randint(0,1)

        if vacuumLocation == 0:
            print("Vacuum is randomly placed at Location A.")
            
            if Environment.locationCondition['A'] == 1:
              print("Location A is Dirty.")
              Environment.locationCondition['A'] = 0
              print("Location A has been changed. ")
              print("Moving to Location B...")

              if Environment.locationCondition['B'] == 1:
                  print("Location B is dirty. ")
                  Environment.locationCondition['B'] = 0
                  print("Location B has been Cleaned. ")

            else:
                print("Moving to Location B...")
                if Environment.locationCondition['B'] == 1:
                    print("Location B is dirty. ")
                    Environment.locationCondition['B'] = 0
                print("Location B has been Cleaned.")

        elif vacuumLocation == 1:
            print("Vacuum is randomly placed at Location B.")
            
            if Environment.locationCondition['B'] == 1:
              print("Location B is Dirty.")
              Environment.locationCondition['B'] = 0
              print("Location B has been changed. ")
              print("Moving to Location A...")

              if Environment.locationCondition['A'] == 1:
                  print("Location A is dirty. ")
                  Environment.locationCondition['B'] = 0
                  print("Location A has been Cleaned. ")

            else:
                print("Moving to Location A...")
                if Environment.locationCondition['A'] == 1:
                    print("Location A is dirty. ")
                    Environment.locationCondition['A'] = 0
                print("Location A has been Cleaned.")

        print(Environment.locationCondition)


rangeLoop = random.randint(1,5)
for Environment.locationCondition in range(rangeLoop):
    theEnvironment = Environment()
    theVacuum = LightVacuumAgent(theEnvironment)
    theVacuum = ThoroughVacuumAgent(theEnvironment)
    