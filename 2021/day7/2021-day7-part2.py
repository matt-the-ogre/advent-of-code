# Advent of Code - 2021 - Day 7

# https://adventofcode.com/2021/day/7


import time, math, logging ,os


def readInput(inputTextFileName):
    # global inputList

    # logging.debug("Don't forget to update your input file path")
    with open(inputTextFileName,"r", encoding='utf-8') as file:
        inputList = file.readlines()

    # remove newlines
    for i in range(0, len(inputList)):
        inputList[i] = inputList[i].rstrip()

    inputList = inputList[0].split(",")

    # logging.debug(f"inputList: {inputList}")

    # convert strings to integers
    inputList = list(map(int,inputList))

    # logging.debug(f"inputList: {inputList}")

    return(inputList)

def processInput(inputList):

    # don't forget to reference global variables here if needed
    # ---

    # make a new list that is going to count the number of crabs at each position

    logging.debug(f"inputList maximum value: {max(inputList)}")

    crabCountList = [0] * (max(inputList)+1)

    for listItem in inputList:
        crabCountList[listItem] += 1

    logging.debug(f"crabCountList: {crabCountList}")

    # figure out the fuel cost for each position, i.e. fuel cost to move all crabs to that position
    fuelCostList = [0] * len(crabCountList)
    logging.debug(f"fuelCostList: {fuelCostList}")

    # okay, back to first principles.
    # for each position, calculate the total cost of fuel to move all crabs there
    # that total cost is the cost of moving each crab in crabCountList to that fuel position index (note: more than one crab per position possible)
    # from Stack Overflow Math, formula for n + (n-1) + (n-2) ... + 1
    # n*(n-1)/2
    #
    # formula for fuel cost is something like
    # n in this case is abs(crabPosition - fuelPosition), or, the nuber of steps required to get the crab to that position
    # abs(crabPosition - fuelPosition) * (abs(crabPosition - fuelPosition) - 1) /2
    # note: we have to add one because we are starting at zero

    # loop through all fuel positions
    for fuelPosition in range(0,len(fuelCostList)):
        # loop through all the crab positions compared to this fuel position
        for crabPosition, crabCount in enumerate(crabCountList):
            if crabCount:
                # calculate difference
                numberOfSteps = abs(fuelPosition - crabPosition) + 1 # adding one here because we start counting at zero
                # calculate cost
                fuelCost = int(numberOfSteps * (numberOfSteps - 1) / 2)
                # multiply by number of crabs
                fuelCost *= crabCount
                # add that fuel cost to that point in the index
                fuelCostList[fuelPosition] += fuelCost
    
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

    answer = int(min(fuelCosts))

    logging.debug(f"answer: {answer}")

    if unitTesting:
        testPass = False

        # write the assignment of a boolean here that will determine if the unit test passed or not
        # logging.debug("Don't forget to update your unit test here.")
        testPass = (answer == 168)

        print("testPass:", testPass)
    else:
        # print the answer here
        # logging.debug("Don't forget to update your print statement of the output here.")
        print(answer)

    # this answer for my input is 94017638

    endTime = time.perf_counter() # time in seconds (float)

    if timing:
        logging.info(f"Execution took {endTime - startTime} seconds.")

if __name__ == '__main__':
    main()
