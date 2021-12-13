# Advent of Code - 2021 - Day 6

# https://adventofcode.com/2021/day/6


import time, math, logging ,os

def readInput(inputTextFileName):
    # global inputList

    logging.debug("Don't forget to update your input file path")
    with open(inputTextFileName,"r", encoding='utf-8') as file:
        inputList = file.readlines()

    # remove newlines
    for i in range(0, len(inputList)):
        inputList[i] = inputList[i].rstrip()

    inputList = inputList[0].split(",")

    logging.debug(f"inputList: {inputList}")

    for index, item in enumerate(inputList):
        inputList[index] = int(item)

    logging.debug(f"inputList: {inputList}")

    return(inputList)

def processInput(inputList):

    # don't forget to reference global variables here if needed
    # ---

    newList = [0,0,0,0,0,0,0,0,0]

    newList = inputList[1:] # newList elements 0 through 8 are just from the inputList elements 1 through 9 (shift a day closer to reproducing)
    newList[6] += inputList[0] # same fish restarts its reproductive timer, add to the fish that just moved to day 7
    newList.append(inputList[0]) # new fish starts with 8 days to reproduce

    assert len(newList) == 9, "length of newList is not 9"

    return(newList)

def main():
    startTime = time.perf_counter() # time in seconds (float)

    # level = logging.DEBUG
    level = logging.INFO
    # level = logging.ERROR
    fmt = '[%(levelname)s] %(asctime)s - %(message)s'
    logging.basicConfig(level=level, format=fmt)

    # get the filepath to load the input files
    filepath = os.path.dirname(__file__)

    timing = True
    unitTesting = False
    inputList = []

    # day-specific variables go here
    numberOfDays = 256
    # ---
    
    if unitTesting:
        logging.info("Unit Testing")
        inputList = readInput(f"{filepath}/unit-test-input.txt")
    else:
        # read the input text file into a variable
        inputList = readInput(f"{filepath}/input.txt")

    # refactor the list so that the index of the list contains the number of fish at that day of their lives
    fishList = [0,0,0,0,0,0,0,0,0]

    for item in inputList:
        fishList[item] += 1
    
    logging.debug(f"day: {numberOfDays} fishList: {fishList} sum(fishList) {sum(fishList)}")

    while numberOfDays > 0:
        fishList = processInput(fishList)
        numberOfDays -= 1
        logging.debug(f"day: {numberOfDays} fishList: {fishList} sum(fishList) {sum(fishList)}")


    answer = sum(fishList)

    logging.debug(f"answer: {answer}")

    if unitTesting:
        testPass = False

        # write the assignment of a boolean here that will determine if the unit test passed or not
        # logging.debug("Don't forget to update your unit test here.")
        testPass = (answer == 26984457539)

        print("testPass:", testPass)
    else:
        # print the answer here
        # logging.debug("Don't forget to update your print statement of the output here.")
        print(answer)

    # this answer for my input is 

    endTime = time.perf_counter() # time in seconds (float)

    if timing:
        logging.info(f"Execution took {endTime - startTime} seconds.")

if __name__ == '__main__':
    main()
