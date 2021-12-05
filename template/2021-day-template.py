# Advent of Code - 2021 - Day X

# https://adventofcode.com/2021/day/X


import time, math, logging


def readInput(inputTextFileName):
    # global inputList

    logging.debug("Don't forget to update your input file path")
    with open("template/"+inputTextFileName,"r", encoding='utf-8') as file:
        inputList = file.readlines()

    # remove newlines
    for i in range(0, len(inputList)):
        inputList[i] = inputList[i].rstrip()

    return(inputList)

def processInput(inputList):

    # don't forget to reference global variables here if needed
    global inputStringLength
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
    timing = False
    unitTesting = False
    inputList = []

    # day-specific variables go here
    # ---
    
    if unitTesting:
        logging.info("Unit Testing")
        inputList = readInput("unit-test-input.txt")
    else:
        # read the input text file into a variable
        inputList = readInput("input.txt")

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
        logging.debug(f"Execution took {endTime - startTime} seconds.")

if __name__ == '__main__':
    main()
