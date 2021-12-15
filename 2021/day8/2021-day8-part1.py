# Advent of Code - 2021 - Day 8

# https://adventofcode.com/2021/day/8


import time, math, logging ,os
from types import prepare_class


def readInput(inputTextFileName):
    # global inputList

    with open(inputTextFileName,"r", encoding='utf-8') as file:
        inputList = file.readlines()

    # remove newlines
    inputList = [listItem.rstrip() for listItem in inputList]

    inputList = [listItem.split(' | ') for listItem in inputList]

    for lineIndex, lineList in enumerate(inputList):
        inputList[lineIndex][1] = lineList[1].split(' ')
    
    return(inputList)

def processInput(inputList):

    # don't forget to reference global variables here if needed
    # ---
    uniqueDigitsCount = 0

    for inputLine, outputLineList in inputList:
        for outputDigit in outputLineList:
            # logging.debug(f"outputDigit: {outputDigit} len(outputDigit): {len(outputDigit)}")
            if len(outputDigit) == 2:
                # digit 1
                uniqueDigitsCount += 1
            elif len(outputDigit) == 3:
                # digit 7
                uniqueDigitsCount += 1
            elif len(outputDigit) == 4:
                # digit 4
                uniqueDigitsCount += 1
            elif len(outputDigit) == 7:
                # digit 8
                uniqueDigitsCount += 1

    return(uniqueDigitsCount)

def main():
    startTime = time.perf_counter() # time in seconds (float)

    level = logging.DEBUG
    # level = logging.INFO
    # level = logging.ERROR
    fmt = '[%(levelname)s] %(asctime)s - %(message)s'
    logging.basicConfig(level=level, format=fmt)

    # get the filepath to load the input files
    filepath = os.path.dirname(__file__)

    timing = True
    unitTesting = False
    inputList = []

    # day-specific variables go here
    # ---
    
    if unitTesting:
        logging.info("Unit Testing")
        inputList = readInput(f"{filepath}/unit-test-input.txt")
    else:
        # read the input text file into a variable
        inputList = readInput(f"{filepath}/input.txt")

    answer = processInput(inputList)

    logging.debug(f"answer: {answer}")

    if unitTesting:
        testPass = False

        # write the assignment of a boolean here that will determine if the unit test passed or not
        # logging.info("Don't forget to update your unit test here.")
        testPass = (answer ==26)

        print("testPass:", testPass)
    else:
        # print the answer here
        # logging.info("Don't forget to update your print statement of the output here.")
        print(answer)

    # this answer for my input is 416

    endTime = time.perf_counter() # time in seconds (float)

    if timing:
        logging.info(f"Execution took {endTime - startTime} seconds.")

if __name__ == '__main__':
    main()
