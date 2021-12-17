# Advent of Code - 2021 - Day X

# https://adventofcode.com/2021/day/X


import time, math, logging, os


def readInput(inputTextFileName):
    # global inputList

    with open(inputTextFileName,"r", encoding='utf-8') as file:
        inputList = file.readlines()

    # remove newlines
    inputList = [listItem.rstrip() for listItem in inputList]
    
    return(inputList)

def processInput(inputList):

    # don't forget to reference global variables here if needed
    # ---
    
    for listItem in inputList:
        logging.debug(f"listItem: {listItem}")
        pass

    return()

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

    processInput(inputList)

    if unitTesting:
        testPass = False

        # write the assignment of a boolean here that will determine if the unit test passed or not
        logging.debug("Don't forget to update your unit test here.")
        testPass = (False)

        print("testPass:", testPass)
    else:
        # print the answer here
        logging.debug("Don't forget to update your print statement of the output here.")
        print(math.nan)

    # this answer for my input is 

    endTime = time.perf_counter() # time in seconds (float)

    if timing:
        logging.info(f"Execution took {endTime - startTime} seconds.")

if __name__ == '__main__':
    main()
