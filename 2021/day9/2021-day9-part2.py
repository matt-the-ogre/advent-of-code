# Advent of Code - 2021 - Day 9

# https://adventofcode.com/2021/day/9



import time, math, logging, os, numpy
from operator import add
from matplotlib import pyplot as plt

def readInput(inputTextFileName):
    # global inputList

    # with open(inputTextFileName,"r", encoding='utf-8') as file:
    #     inputList = file.readlines()

    # # remove newlines
    # inputList = [listItem.rstrip() for listItem in inputList]
    
    # note I'm cheating a bit because I regex'd the input into a CSV format
    # search "\d" replace "$0,"; search ",\n" replace "\n"
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

    logging.debug(f"inputArray\n{inputArray[0:2]}")

    # also just for fun, display the array as an image
    # logging.basicConfig(level=logging.INFO)
    # plt.gray()
    # plt.imshow(inputArray.squeeze())
    # plt.show()
    # logging.basicConfig(level=logging.DEBUG)

    return(inputArray)

def checkNeighbourAllLower(locationTuple):
    global inputArray
    neighboursAllLower = False

    # note: good question and answer on tuple arithmetic
    # https://stackoverflow.com/questions/17418108/elegant-way-to-perform-tuple-arithmetic

    # using `numpy` is measurably slower than `map` and `add`
    # left = tuple(numpy.add(locationTuple,  (-1, 0)))
    # right = tuple(numpy.add(locationTuple,  (1, 0)))
    # up = tuple(numpy.add(locationTuple,  (0, -1)))
    # down = tuple(numpy.add(locationTuple,  (0, 1)))
    left = tuple(map(add, locationTuple,  (-1, 0)))
    right = tuple(map(add, locationTuple,  (1, 0)))
    up = tuple(map(add, locationTuple,  (0, -1)))
    down = tuple(map(add, locationTuple,  (0, 1)))

    # logging.debug(f"locationTuple: {locationTuple} left: {left}")

    listOfNeighbours = [ inputArray[left], inputArray[right], inputArray[up], inputArray[down] ]

    neighboursAllLower = inputArray[locationTuple] < min(listOfNeighbours)

    return neighboursAllLower

def basinSize(locationTuple):
    global inputArray, basinElements

    if inputArray[locationTuple] == 9:
        # locations with height 9 are not ever in a basin
        return 0
    elif locationTuple in basinElements:
        # already counted this one, don't double-count
        return 0
    else:
        # this element is in a basin
        thisBasinSize = 1
        # add this location to the already in a basin list so we don't double count it
        basinElements.append(locationTuple)
    
        left = tuple(map(add, locationTuple,  (-1, 0)))
        right = tuple(map(add, locationTuple,  (1, 0)))
        up = tuple(map(add, locationTuple,  (0, -1)))
        down = tuple(map(add, locationTuple,  (0, 1)))

        # recursively check the cross neighbours for their basin size
        thisBasinSize += basinSize(left)
        thisBasinSize += basinSize(right)
        thisBasinSize += basinSize(up)
        thisBasinSize += basinSize(down)
    return thisBasinSize

def processInput():

    # don't forget to reference global variables here if needed
    global inputArray
    # ---
    
    basinSizeList = []
    for index,element in numpy.ndenumerate(inputArray):
        # skip the first and last row, and the first and last column because they were synthetically added
        # to make the neighbour checking easier (all 9s)
        if index[0] != 0 and index[0] != inputArray.shape[0]-1 and index[1] != 0 and index[1] != inputArray.shape[1]-1:
            # logging.debug(f"index: {index} element: {element}")
            if checkNeighbourAllLower(index):
                basinSizeList.append(basinSize(index))
                pass

    # test
    # basinSizeList = [3,9,14,9]
    logging.debug(f"basinSizeList: {basinSizeList}")
    threeLargestBasins = 1
    for i in range(3):
        threeLargestBasins *= max(basinSizeList)
        basinSizeList.remove(max(basinSizeList))

    return(threeLargestBasins)

def main():
    startTime = time.perf_counter() # time in seconds (float)

    global inputArray
    global basinElements
    
    level = logging.DEBUG
    # level = logging.INFO
    # level = logging.ERROR
    fmt = '[%(levelname)s] %(asctime)s - %(message)s'
    logging.basicConfig(level=level, format=fmt)

    # get the filepath to load the input files
    filepath = os.path.dirname(__file__)

    timing = True
    unitTesting = False
    inputArray = []
    basinElements = []

    # day-specific variables go here
    # ---
    
    if unitTesting:
        logging.info("Unit Testing")
        inputArray = readInput(f"{filepath}/unit-test-input.txt")
    else:
        # read the input text file into a variable
        inputArray = readInput(f"{filepath}/input.txt")

    threeLargestBasins = processInput()

    if unitTesting:
        testPass = False

        # write the assignment of a boolean here that will determine if the unit test passed or not
        # logging.debug("Don't forget to update your unit test here.")
        testPass = (threeLargestBasins == 1134)

        print("testPass:", testPass)
    else:
        # print the answer here
        # logging.debug("Don't forget to update your print statement of the output here.")
        print(threeLargestBasins)

    # this answer for my input is 494

    endTime = time.perf_counter() # time in seconds (float)

    if timing:
        logging.info(f"Execution took {endTime - startTime} seconds.")

if __name__ == '__main__':
    main()
