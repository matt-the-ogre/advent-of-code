# Advent of Code - 2021 - Day X

# https://adventofcode.com/2021/day/X


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

    # for index, item in enumerate(inputList):
    #     inputList[index] = int(item)
    # could use:
    inputList = list(map(int,inputList))

    logging.debug(f"inputList: {inputList}")

    return(inputList)

def processInput(inputList):

    # don't forget to reference global variables here if needed
    # ---

    # make a new list that is going to count the number of crabs at each position

    logging.debug(f"inputList maximum value: {max(inputList)}")

    # newList = range(0,max(inputList)+1)
    crabCountList = [0] * (max(inputList)+1)

    for listItem in inputList:
        logging.debug(f"listItem: {listItem}")
        crabCountList[listItem] += 1

    logging.debug(f"newList: {crabCountList}")

    # figure out the fuel cost for each position, i.e. fuel cost to move all crabs to that position
    fuelCostList = [0] * len(crabCountList)

    for fuelIndex, item in enumerate(fuelCostList):
        fuelCost = 0
        for crabIndex, crabCount in enumerate(crabCountList):
            fuelCost += crabCount * abs(crabIndex - fuelIndex)
        fuelCostList[fuelIndex] += fuelCost
    
    logging.debug(f"fuelCostList: {fuelCostList}")

    return(fuelCostList)

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
    # ---
    
    if unitTesting:
        logging.info("Unit Testing")
        inputList = readInput(f"{filepath}/unit-test-input.txt")
    else:
        # read the input text file into a variable
        inputList = readInput(f"{filepath}/input.txt")

    fuelCosts = processInput(inputList)

    answer = min(fuelCosts)

    if unitTesting:
        testPass = False

        # write the assignment of a boolean here that will determine if the unit test passed or not
        # logging.debug("Don't forget to update your unit test here.")
        testPass = (answer == 37)

        print("testPass:", testPass)
    else:
        # print the answer here
        # logging.debug("Don't forget to update your print statement of the output here.")
        print(answer)

    # this answer for my input is 333755

    endTime = time.perf_counter() # time in seconds (float)

    if timing:
        logging.info(f"Execution took {endTime - startTime} seconds.")

if __name__ == '__main__':
    main()
