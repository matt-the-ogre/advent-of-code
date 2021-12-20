# Advent of Code - 2021 - Day 11

# https://adventofcode.com/2021/day/11


import time, math, logging, os, numpy
from operator import add
from matplotlib import pyplot as plt

def readInput(inputTextFileName):
    global inputArray
    
    # note I'm cheating a bit because I regex'd the input into a CSV format
    # search "\d" replace "$0,"; search ",\n" replace "\n"
    inputArray = numpy.loadtxt(inputTextFileName, dtype=int, delimiter=',')

    # logging.debug(f"first row: {inputArray[0]}")

    # let's pad with nan's to make our neighbour logic easier
    sizeTuple = inputArray.shape
    logging.debug(f"size: {sizeTuple}")
    rowOfNines = numpy.full((1,sizeTuple[1]), math.nan)
    columnOfNines = numpy.full((sizeTuple[0]+2,1), math.nan) # note: +2 because we are going to add two rows to the input array
    # logging.debug(f"rowOfNines: {rowOfNines}, columnOfNines: f{columnOfNines}")

    # append rows
    inputArray = numpy.append(rowOfNines, inputArray, axis=0)
    inputArray = numpy.append(inputArray, rowOfNines, axis=0)
    
    # append columns
    inputArray = numpy.append(columnOfNines, inputArray, axis=1)
    inputArray = numpy.append(inputArray, columnOfNines, axis=1)

    logging.debug(f"inputArray\n{inputArray[0:2]}")

    return(inputArray)

def flashElement(locationTuple):
    # flash the current element and increment its neighbours
    global inputArray
    global hasFlashedArray
    hasFlashedArray[locationTuple] += 1

    # logging.debug(f"Flashing element: {locationTuple}")
    # note: good question and answer on tuple arithmetic
    # https://stackoverflow.com/questions/17418108/elegant-way-to-perform-tuple-arithmetic

    # using `numpy` is measurably slower than `map` and `add`
    selfLocation = locationTuple
    left = tuple(map(add, locationTuple,  (-1, 0)))
    right = tuple(map(add, locationTuple,  (1, 0)))
    up = tuple(map(add, locationTuple,  (0, -1)))
    down = tuple(map(add, locationTuple,  (0, 1)))
    upleft = tuple(map(add, locationTuple,  (-1, -1)))
    upright = tuple(map(add, locationTuple,  (1, -1)))
    downleft = tuple(map(add, locationTuple,  (-1, 1)))
    downright = tuple(map(add, locationTuple,  (1, 1)))

    # subArray = inputArray[upleft, tuple(map(add, downright, (1,1)))]
    subArray = inputArray[upleft,  downright]
    # logging.debug(f"neighbourhood before flashing:\n{subArray}")

    listOfNeighbourTuples = [left, right, up, down, upleft, upright, downleft, downright]
    for positionTuple in listOfNeighbourTuples:
        inputArray[positionTuple] += 1

    # logging.debug(f"neighbourhood after flashing:\n{subArray}")
    return

def processInput():

    # don't forget to reference global variables here if needed
    global inputArray
    global hasFlashedArray
    global funWithGraphics
    global filepath

    hasFlashedArray = numpy.zeros(inputArray.shape, dtype=int)
    # ---
    totalFlashes = 0

    # for listItem in inputArray:
    #     logging.debug(f"listItem: {listItem}")
    #     pass

    totalSteps = 100
    for stepNum in range(totalSteps):
        hasFlashedArray = numpy.zeros(inputArray.shape, dtype=int)

        # add one to every element in the array
        # logging.debug(f"\n{inputArray[1:3]}")
        inputArray += 1
        # logging.debug(f"every array element increased by 1\n{inputArray[1:3]}")
        # we need to successively iterate over this array until every element that is over energy level 9 and 
        # hasn't flashed this step is flashed
        somethingFlashed = True
        while somethingFlashed:
            somethingFlashed = False
            for index,element in numpy.ndenumerate(inputArray):
                # don't process rows 1 and n and columns 1 and n
                if index[0] != 0 and index[0] != inputArray.shape[0]-1 and index[1] != 0 and index[1] != inputArray.shape[1]-1:
                    # logging.debug(f"index: {index}")
                    assert (index > (0,0) and index < (inputArray.shape)), "index out of bounds"
                    # only flash an element if it's energy level is greater than 9 and it hasn't flashed this step
                    if element > 9 and element != math.nan and hasFlashedArray[index] == 0:
                        flashElement(index)
                        totalFlashes += 1
                        somethingFlashed = True
        
        # now return anything 9 or greater back to zero energy level
        for index,element in numpy.ndenumerate(inputArray):
            if element > 9 and element != math.nan:
                inputArray[index] = 0

        # logging.debug(f"inputArray\n{inputArray}")

        # logging.debug(f"totalFlashes: {totalFlashes}")
        # also just for fun, display the array as an image
        # logging.basicConfig(level=logging.INFO)
        if funWithGraphics:
            plt.gray()
            plt.imshow(inputArray.squeeze())
            plt.title(f"Step {stepNum}")
            plt.savefig(f"{filepath}\images\dumbo{stepNum}.png")
        # plt.show()
        # logging.basicConfig(level=logging.DEBUG)



    # logging.debug(f"\n{inputArray}")

    return(totalFlashes)

def main():
    startTime = time.perf_counter() # time in seconds (float)

    # level = logging.DEcdBUG
    level = logging.INFO
    # level = logging.ERROR
    fmt = '[%(levelname)s] %(asctime)s - %(message)s'
    logging.basicConfig(level=level, format=fmt)

    # get the filepath to load the input files
    global filepath
    global funWithGraphics

    filepath = os.path.dirname(__file__)

    timing = True
    unitTesting = False
    funWithGraphics = False

    # day-specific variables go here
    global inputArray
    global hasFlashedArray
    # inputArray = []
    totalFlashes = 0
    # ---
    
    if unitTesting:
        logging.info("Unit Testing")
        inputArray = readInput(f"{filepath}/unit-test-input.txt")
    else:
        # read the input text file into a variable
        inputArray = readInput(f"{filepath}/input.txt")

    totalFlashes = processInput()

    if unitTesting:
        testPass = False

        # write the assignment of a boolean here that will determine if the unit test passed or not
        testPass = (totalFlashes == 1656)

        print("testPass:", testPass)
    else:
        # print the answer here
        print(totalFlashes)

    # this answer for my input is 

    endTime = time.perf_counter() # time in seconds (float)

    if timing:
        logging.info(f"Execution took {endTime - startTime} seconds.")

    if funWithGraphics:
        output = os.system(f"magick convert -delay 20 {filepath}\images\*.png anim.mp4")
        logging.debug(f"{output}")


if __name__ == '__main__':
    main()
