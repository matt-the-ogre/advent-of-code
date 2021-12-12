# Advent of Code - 2016 - Day 1

# https://adventofcode.com/2016/day/1


import time, math, logging, os


def readInput(inputTextFileName):
    # global inputList

    logging.debug("Don't forget to update your input file path")
    with open(inputTextFileName,"r", encoding='utf-8') as file:
        inputList = file.readlines()

    # remove newlines
    inputList = [listItem.rstrip() for listItem in inputList]

    inputList = [listItem.replace(" ", "") for listItem in inputList]

    inputList = [listItem.split(",") for listItem in inputList]


    return(inputList)

def processInput(inputList):

    
    # don't forget to reference global variables here if needed
    # ---
    startX = 0
    startY = 0
    startDirection = "N"
    directionDict = {"R": {"N": "E", "E": "S", "S": "W", "W" : "N"}, "L": {"N": "W", "W": "S", "S": "E", "E": "N"}}
    currentDirection = startDirection

    for listItem in inputList:
        logging.debug(f"listItem: {listItem}")
        for step in listItem:
            logging.debug(f"step: {step}")
            turn =  4444

            
            logging.debug(f"turn: {turn}")
            
            newDirection = directionDict[turn][currentDirection]
            logging.debug(f"newDirection: {newDirection}")
        pass

    blocksAway = 0

    return(blocksAway)

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
    unitTesting = True
    inputList = []

    # day-specific variables go here
    # ---
    
    if unitTesting:
        logging.info("Unit Testing")
        inputList = readInput(f"{filepath}/unit-test-input.txt")
    else:
        # read the input text file into a variable
        inputList = readInput(f"{filepath}/input.txt")

    blocksAway = processInput(inputList)

    if unitTesting:
        testPass = False

        # write the assignment of a boolean here that will determine if the unit test passed or not
        logging.debug("Don't forget to update your unit test here.")
        testPass = (blocksAway == 12)

        print("testPass:", testPass)
    else:
        # print the answer here
        logging.debug("Don't forget to update your print statement of the output here.")
        print(math.nan)

    # this answer for my input is 

    endTime = time.perf_counter() # time in seconds (float)

    if timing:
        logging.debug(f"Execution took {endTime - startTime} seconds.")

if __name__ == '__main__':
    main()
