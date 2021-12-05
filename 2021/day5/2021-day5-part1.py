# Advent of Code - 2021 - Day 5

# https://adventofcode.com/2021/day/5


import time, math, logging, os, numpy


def readInput(inputTextFileName):
    with open(inputTextFileName,"r", encoding='utf-8') as file:
        inputList = file.readlines()

    # remove newlines
    inputList = [listItem.rstrip() for listItem in inputList]

    return(inputList)

def processInput(inputList):

    # don't forget to reference global variables here if needed
    # gridArray = numpy.array(len(inputList[0],len(inputList)))
    # ---

    maxX = 0
    maxY = 0

    tupleList = []

    # convert from list of strings to lists of tuples
    for listItem in inputList:
        # logging.debug(f"listItem: {listItem}")
        firstTuple = tuple([int(xItem) for xItem in listItem.split(" -> ")[0].split(",")])
        secondTuple = tuple([int(xItem) for xItem in listItem.split(" -> ")[1].split(",")])
        # logging.debug(f"{firstTuple} to {secondTuple}")
        tupleList.append([firstTuple,secondTuple])
        if firstTuple[0] > maxX:
            maxX = firstTuple[0]
        if firstTuple[1] > maxY:
            maxY = firstTuple[1]
        if secondTuple[0] > maxX:
            maxX = secondTuple[0]
        if secondTuple[1] > maxY:
            maxY = secondTuple[1]

    # logging.debug(f"{tupleList}")
    tupleList.sort()
    # logging.debug(f"{tupleList}")
    # logging.debug(f"maxX: {maxX} maxY: {maxY}")
    if len(inputList) != len(tupleList):
        logging.error(f"tupleList is different length than inputList: {len(tupleList)} vs. {len(inputList)}") 

    gridArray = numpy.zeros((maxX+1,maxY+1)) # have to add one to the size because we are zero-indexed
    # logging.debug(f"\n{gridArray}")

    for pairItem in tupleList:
        # only consider horizontal or vertical lines
        if (pairItem[0][0] == pairItem[1][0]) or (pairItem[0][1] == pairItem[1][1]):
            # logging.debug(f"adding pairItem: {pairItem}")
            lowXRange = min(pairItem[0][0],pairItem[1][0])
            highXRange = max(pairItem[0][0],pairItem[1][0])
            for x in range(lowXRange,highXRange+1):
                lowYRange = min(pairItem[0][1],pairItem[1][1])
                highYRange = max(pairItem[0][1],pairItem[1][1])
                for y in range(lowYRange,highYRange+1):
                    # logging.debug(f"({x},{y})")
                    gridArray[x,y] += 1
        else:
            # logging.debug(f"skipping pairItem: {pairItem}")
            pass
    logging.debug(f"\n{gridArray}")

    pointsOverlap = len(gridArray[gridArray > 1])
    # logging.debug(f"points where two lines overlap = {pointsOverlap}")
    return(pointsOverlap)

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

    # logging.debug(f"{len(inputList)}")

    pointsOverlap = processInput(inputList)

    if unitTesting:
        testPass = False

        # write the assignment of a boolean here that will determine if the unit test passed or not
        # logging.debug("Don't forget to update your unit test here.")
        testPass = (pointsOverlap == 5)

        print("testPass:", testPass)
    else:
        # logging.debug the answer here
        # logging.debug("Don't forget to update your print statement of the output here.")
        print(pointsOverlap)

    # this answer for my input is 

    endTime = time.perf_counter() # time in seconds (float)

    if timing:
        logging.info(f"Execution took {endTime - startTime} seconds.")

if __name__ == '__main__':
    main()
