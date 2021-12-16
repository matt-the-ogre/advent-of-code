# Advent of Code - 2021 - Day X

# https://adventofcode.com/2021/day/X


import time, math, logging, os, numpy


def readInput(inputTextFileName):
    # global inputList

    # with open(inputTextFileName,"r", encoding='utf-8') as file:
    #     inputList = file.readlines()

    # # remove newlines
    # inputList = [listItem.rstrip() for listItem in inputList]
    
    # note I'm cheating a bit because I regex'd the input into a CSV format
    inputArray = numpy.loadtxt(inputTextFileName, dtype=int, delimiter=',')

    logging.debug(f"first row: {inputArray[0]}")

    # let's pad with 9s to make our neighbour logic easier
    sizeTuple = inputArray.shape
    logging.debug(f"size: {sizeTuple}")
    rowOfNines = numpy.full((1,sizeTuple[1]), 9)
    columnOfNines = numpy.full((sizeTuple[0]+2,1), 9) # note: +2 because we are going to add two rows to the input array
    # logging.debug(f"rowOfNines: {rowOfNines}, columnOfNines: f{columnOfNines}")

    # append rows
    inputArray = numpy.append(rowOfNines, inputArray, axis=0)
    inputArray = numpy.append(inputArray, rowOfNines, axis=0)
    
    # append columns
    inputArray = numpy.append(columnOfNines, inputArray, axis=1)
    inputArray = numpy.append(inputArray, columnOfNines, axis=1)

    logging.debug(f"inputArray\n{inputArray}")

    return(inputArray)

def checkNeighbourAllLower(locationTuple):
    global inputArray
    neighboursAllLower = False
    x = locationTuple[0]
    y = locationTuple[1]

    listOfNeighbours = [ inputArray[x-1,y], inputArray[x+1,y], inputArray[x,y-1], inputArray[x,y+1] ]

    myValue = inputArray[locationTuple]
    minNeighbours = min(listOfNeighbours)
    logging.debug(f"myValue: {myValue}, minNeighbours: {minNeighbours}")

    neighboursAllLower = myValue < minNeighbours

    logging.debug(f"height: {inputArray[x][y]} neighbours: {listOfNeighbours} neighboursAllLower: {neighboursAllLower}")

    return neighboursAllLower

def processInput():

    # don't forget to reference global variables here if needed
    global inputArray
    # ---
    
    riskLevelSum = 0
    for index,element in numpy.ndenumerate(inputArray):
        if index[0] != 0 and index[0] != inputArray.shape[0]-1 and index[1] != 0 and index[1] != inputArray.shape[1]-1:
            logging.debug(f"index: {index} element: {element}")
            if checkNeighbourAllLower(index):
                riskLevelSum += 1 + element

    return(riskLevelSum)

def main():
    startTime = time.perf_counter() # time in seconds (float)

    global inputArray

    # level = logging.DEBUG
    level = logging.INFO
    # level = logging.ERROR
    fmt = '[%(levelname)s] %(asctime)s - %(message)s'
    logging.basicConfig(level=level, format=fmt)

    # get the filepath to load the input files
    filepath = os.path.dirname(__file__)

    timing = True
    unitTesting = False
    inputArray = []

    # day-specific variables go here
    # ---
    
    if unitTesting:
        logging.info("Unit Testing")
        inputArray = readInput(f"{filepath}/unit-test-input.txt")
    else:
        # read the input text file into a variable
        inputArray = readInput(f"{filepath}/input.txt")

    riskLevel = processInput()

    if unitTesting:
        testPass = False

        # write the assignment of a boolean here that will determine if the unit test passed or not
        logging.debug("Don't forget to update your unit test here.")
        testPass = (riskLevel == 15)

        print("testPass:", testPass)
    else:
        # print the answer here
        logging.debug("Don't forget to update your print statement of the output here.")
        print(riskLevel)

    # this answer for my input is 494

    endTime = time.perf_counter() # time in seconds (float)

    if timing:
        logging.info(f"Execution took {endTime - startTime} seconds.")

if __name__ == '__main__':
    main()
