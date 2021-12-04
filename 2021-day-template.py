# Advent of Code - 2021 - Day 4

# https://adventofcode.com/2021/day/4


import time, math

startTime = time.time() # time in seconds (float)

debug = False
timing = False
unitTesting = False
inputList = []

# day-specific variables go here
# ---

def readInput(inputTextFileName):
    global inputList

    with open("2021/day4/"+inputTextFileName,"r", encoding='utf-8') as file:
        inputList = file.readlines()

    # remove newlines
    for i in range(0, len(inputList)):
        inputList[i] = inputList[i].rstrip()

    return()

def processInput(inputList):

    # don't forget to reference global variables here if needed
    global inputStringLength
    # ---
    for listItem in inputList:
        if debug:
            print("listItem:",listItem)
        pass

    return()

if unitTesting:
    print("Unit Testing")
    inputList = readInput("unit-test-input.txt")
else:
    # read the input text file into a variable
    inputList = readInput("input.txt")

processInput(inputList)

if unitTesting:
    testPass = False

    # write the assignment of a boolean here that will determine if the unit test passed or not
    testPass = (False)

    print("testPass:", testPass)
else:
    # print the answer here
    print(math.nan)

# this answer for my input is 

endTime = time.time() # time in seconds (float)

if timing:
    print("Execution took ", endTime - startTime, " seconds.")

