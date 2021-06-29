import sys
"""The Environment"""
class Environment(object):

    loc = ['11', '12', '13','14','21', '22', '23','24','31', '32', '33','34','41', '42', '43','44']
    wumpus='13'
    pit=['31','33','44']
    move = ['U','D','L','R']
    Agent_loc='11'
    Agent_arrow=True
    Agent_gold=True
    gold=['23']
    
    kb= {  '11':['F','F','F','F','F','F'], '12':['F','F','F','F','F','F'],
           '13':['F','F','F','F','F','F'], '14':['F','F','F','F','F','F'],
           '21':['F','F','F','F','F','F'], '22':['F','F','F','F','F','F'],
           '23':['F','F','F','F','F','F'], '24':['F','F','F','F','F','F'],
           '31':['F','F','F','F','F','F'], '32':['F','F','F','F','F','F'],
           '33':['F','F','F','F','F','F'], '34':['F','F','F','F','F','F'],
           '41':['F','F','F','F','F','F'], '42':['F','F','F','F','F','F'],
           '43':['F','F','F','F','F','F'], '44':['F','F','F','F','F','F']}
    path = {
    "1R":"2","1D":"3","2L":"1","2D":"4",
    "3R":"4","3U":"1","4L":"3","4U":"2",
    "1U":"W","1L":"W","2U":"W","2R":"W",
    "3D":"W","3L":"W","4R":"W","4D":"W"
    }
    neighbours = {  '11':set(['12','21']),      '12':set(['11','22','13']),
                    '13':set(['12','23','14']), '14':set(['13','24']),
                    '21':set(['11','22','31']), '22':set(['12','21','32','23']),
                    '23':set(['13','22','33']), '24':set(['14','23','34']),
                    '31':set(['21','32','41']), '32':set(['22','31','42','33']),
                    '33':set(['23','32','43',   '34']), '34':set(['24','33','44']),
                    '41':set(['31','42']),      '42':set(['32','41','43']),
                    '43':set(['33','42','44']), '44':set(['34','43'])}
    action=[]
    visited=[]
    visited.append(Agent_loc)
class Agent(Environment):
    play=True
    def __init__(self, Environment):
        print("Select H for Human or C for Computer agent" )
        ans=input()
        if ans== 'H':
            while Agent.play:
                Agent.H_Agent()
        elif ans== 'C':
            while Agent.play:
                Agent.KB_Agent()
        else:
            print('Invalid Choice')
    def H_Agent():
        print("select action: m-Move, s-shoot,g-collect,q-quit")
        H_Action=input()
        if H_Action=='m':
            print("Current Location",Environment.Agent_loc)
            print("neighbours",Environment.neighbours[Environment.Agent_loc] )
            print("select cave to move: ",Environment.neighbours[Environment.Agent_loc])
            i=input()
            print("new neighbours",Environment.neighbours[i])
            if i == '13' and Environment.wumpus=='13':
                print("Sorry-You have been Swallowed by Wumpus!!!")
                print("Bye Bye!!!")
            elif i=='31' or i=='33'or i=='44':
                print("Sorry-You have fallen into a bottomless pit!!!")
                print("Bye Bye!!!")
            else:   
                if '13' in Environment.neighbours[i]:
                   if Environment.wumpus=='13':
                        print("--Stench--")
                if '31' in Environment.neighbours[i] or '33' in Environment.neighbours[i] or '44' in Environment.neighbours[i] :
                        print("--Breeze--")
                if '23' in Environment.neighbours[i]:
                        print("--Glitter--")
                Environment.Agent_loc=i
        elif H_Action=='s':
                print("select cave to shoot: ",Environment.neighbours[Environment.Agent_loc])
                i=input()
                if i=='13' and Environment.wumpus=='13'and Environment.Agent_arrow==True:
                    Environment.Agent_arrow=False
                    Environment.wumpus="dead"
                    print("Hoooraaay You killed the Wumpus!!!")
                elif i!='13' and Environment.wumpus=='13'and Environment.Agent_arrow==True:
                    print("Missed!!! You also lost your only arrow!")
                elif Environment.wumpus=='dead':
                     print("The wumpus is already Dead!")
                else:
                     print("You have no more arrows!")
        elif H_Action=='g':
           print(Environment.Agent_gold)
           if Environment.Agent_loc=='23' and Environment.Agent_gold==True:
                print("Hoooraaay You found the Gold!!!")
                Environment.Agent_gold=False
           else:
                print("there is nothing to collect here")
        elif H_Action=='q':
            if Environment.Agent_gold==True:
                print("YOU LOST: Uncollected Gold")
            elif Environment.wumpus=='13':
                print("YOU LOST: The Wumpus is still alive")
            else:
                print("YOU WIN: The Wumpus is dead and you have the Gold")
                print("Goal Reached")
            Agent.play=False
           
"""Create the agent"""
theEnvironment = Environment()
theAgent= Agent(theEnvironment)