import spaceGraph as sg
import os

curSpace = None

def createSpace():
    label = input('Enter the name of the space: ')
    if curSpace == None:
        sg.roots.add(sg.cSpace(label))

def printRoots():
    print(sg.rootLabels())

def show(*arr):
    i = 0
    while i <  len(arr):
        print(arr[i], len(arr[i]))
        i += 1

command = {
            'show' : show,
            'quit' : quit,
            'space' : createSpace,
            'roots' : printRoots
            }

while True:
    commandLine = input('>>> ')
    param = []

    i = 0
    j = 0
    num = 0
    while i < len(commandLine):
        if commandLine[i] == ' ':
            if i != 0:
                if j == 0:
                    subStr = commandLine[:i]
                else:
                    subStr = commandLine[j+1:i]
                if len(subStr) > 0:
                    if num == 0:
                        cmd = subStr
                    else:
                        param.append(subStr)
                    num += 1
            j = i

        if i == len(commandLine)-1:
            if j == 0:
                subStr = commandLine[j:]
            else:
                subStr = commandLine[j+1:]
            
            if len(subStr) > 0:
                if num == 0:
                    cmd = subStr
                else:
                    param.append(subStr)
                num += 1
        
        i += 1
            
    #os.system('cls')
    #print(cmd, len(cmd))
    #print(param)
    if cmd in command:
        command[cmd](*param)
    else:
        print('unkown command')
