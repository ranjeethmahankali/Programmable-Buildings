import spaceGraph as sg
import os

curSpace = None

def createSpace():
    label = input('Enter the name of the space: ')
    if curSpace == None:
        sg.roots.add(sg.cSpace(label))

def printRoots():
    print(sg.rootLabels())

command = {
            'quit' : quit,
            'space' : createSpace,
            'roots' : printRoots
            }

while True:
    commandLine = input('>>> ')
    #os.system('cls')
    if commandLine in command:
        command[commandLine]()
    else:
        print('unkown command')
