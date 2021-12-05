# Advent of Code - 2021 - Day 3

# https://adventofcode.com/2021/day/3

# --- Day 3: Binary Diagnostic ---

# The submarine has been making some odd creaking noises, so you ask it to produce a diagnostic report just in case.

# The diagnostic report (your puzzle input) consists of a list of binary numbers which, when decoded properly, can tell you many useful things about the conditions of the submarine. The first parameter to check is the power consumption.

# You need to use the binary numbers in the diagnostic report to generate two new binary numbers (called the gamma rate and the epsilon rate). The power consumption can then be found by multiplying the gamma rate by the epsilon rate.

# Each bit in the gamma rate can be determined by finding the most common bit in the corresponding position of all numbers in the diagnostic report. For example, given the following diagnostic report:

# 00100
# 11110
# 10110
# 10111
# 10101
# 01111
# 00111
# 11100
# 10000
# 11001
# 00010
# 01010

# Considering only the first bit of each number, there are five 0 bits and seven 1 bits. Since the most common bit is 1, the first bit of the gamma rate is 1.

# The most common second bit of the numbers in the diagnostic report is 0, so the second bit of the gamma rate is 0.

# The most common value of the third, fourth, and fifth bits are 1, 1, and 0, respectively, and so the final three bits of the gamma rate are 110.

# So, the gamma rate is the binary number 10110, or 22 in decimal.

# The epsilon rate is calculated in a similar way; rather than use the most common bit, the least common bit from each position is used. So, the epsilon rate is 01001, or 9 in decimal. Multiplying the gamma rate (22) by the epsilon rate (9) produces the power consumption, 198.

# Use the binary numbers in your diagnostic report to calculate the gamma rate and epsilon rate, then multiply them together. What is the power consumption of the submarine? (Be sure to represent your answer in decimal, not binary.)

import time, math

startTime = time.perf_counter() # time in seconds (float)

debug = False
timing = False
unitTesting = False
inputList = []

# day-specific variables go here
inputStringLength = 0
gammaRateList = []
epsilonRateList = []
gammaRateInt = 0
epsilonRateInt = 0
# ---

def readInput(inputTextFileName):
    global inputStringLength
    inputList = []

    with open("2021/day3/"+inputTextFileName,"r", encoding='utf-8') as file:
        inputList = file.readlines()

    # remove newlines
    for i in range(0, len(inputList)):
        inputList[i] = inputList[i].rstrip()

    inputStringLength = len(inputList[0])

    return(inputList)

def processInput(inputList):

    # for this puzzle I think we can simply add up the columns in the binary number and detemine if that total is greater than or less than half the length of the main list
    # if less than half the length, it means 0 is more common
    # if more than half the length, it means 1 is more common
    # I think epsilon is just the XOR of gamma
        
    # don't forget to reference global variables here if needed
    global inputStringLength
    # ---
    gammaRate = [0] * inputStringLength
    epsilonRate = [1] * inputStringLength

    gammaCount = [0] * inputStringLength

    if debug:
        print("len(inputList):",len(inputList))

    for listItem in inputList:
        for i in range(0,inputStringLength):
            gammaCount[i] += int(listItem[i]) # convert string character to integer for addition
    
    for i in range(0,inputStringLength):
        if (gammaCount[i] > (len(inputList)/2)):
            # greater than half, then it's a "1" for this gammaRate position
            gammaRate[i] = 1
            epsilonRate[i] = 0

    if debug:
        print("gammaRate:",gammaRate,"epsilonRate:",epsilonRate)        

    return(gammaRate, epsilonRate)

if unitTesting:
    print("Unit Testing")
    inputList = readInput("unit-test-input.txt")
else:
    # read the input text file into a variable
    inputList = readInput("input.txt")

(gammaRateList, epsilonRateList) = processInput(inputList)

for i in range(0,inputStringLength,1):

    gammaRateInt += gammaRateList[i] * 2**(inputStringLength-1-i)
    epsilonRateInt += epsilonRateList[i] * 2**(inputStringLength-1-i)

if debug:
    print("gammaRateInt:", gammaRateInt, "epsilonRateInt:", epsilonRateInt)

if unitTesting:
    testPass = False

    # write the assignment of a boolean here that will determine if the unit test passed or not
    testPass = (gammaRateInt * epsilonRateInt == 198)

    print("testPass:", testPass)
else:
    # print the answer here
    print(gammaRateInt * epsilonRateInt)

# this answer for my input is 3969000

endTime = time.perf_counter() # time in seconds (float)

if timing:
    print("Execution took ", endTime - startTime, " seconds.")

