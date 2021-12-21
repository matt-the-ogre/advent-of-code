# Advent of Code - 2021 - Day X

# https://adventofcode.com/2021/day/X


import time, math, logging, os, numpy
from operator import itemgetter
from operator import add, sub

from numpy.lib.function_base import diff

def readInput(inputTextFileName):
    # global inputList

    with open(inputTextFileName,"r", encoding='utf-8') as file:
        inputList = file.readlines()

    # remove newlines
    inputList = [listItem.rstrip() for listItem in inputList]
    
    return(inputList)

def separateInput(inputList):
    dotArray = []
    dotList = []
    foldInstructionList = []

    # start at the bottom of inputList
    for index, line in enumerate(reversed(inputList)):
        logging.debug(f"{index = }\t{line = }")
        if "fold" in line:
            # this is a fold instruction
            # foldInstructionList.append(line)
            foldInstructionList.insert(0, {'axis': line.split('=')[0][-1:], 'value': int(line.split('=')[1])})

        elif len(line) == 0:
            # this is the blank line, do nothing
            pass
        elif "," in line:
            dotList.append((int(line.split(',')[0]), int(line.split(',')[1])))

    logging.debug(f"{dotList[:3] = }\n{foldInstructionList[:2] = }")
    # we should now have dotList and foldInstructions fully populated
    # reverse the fold instructions since we populated it from the bottom
    # foldInstructionList = foldInstructionList.reverse()
    # logging.debug(f"{foldInstructionList[:2] = }")

    # https://stackoverflow.com/questions/13145368/find-the-maximum-value-in-a-list-of-tuples-in-python
    maxX = max(dotList, key=itemgetter(0))[0]
    maxY = max(dotList, key=itemgetter(1))[1]
    logging.debug(f"{maxX = }\t{maxY = }")

    # https://thispointer.com/create-numpy-array-of-different-shapes-initialize-with-identical-values-using-numpy-full-in-python/
    # create an array of the correct size, full of dots
    # note +1 because of zero indexing
    dotArray = numpy.full((maxX+1, maxY+1), 0)
    assert dotArray.shape == (maxX+1, maxY+1), f"dotArray created in wrong shape {dotArray.shape =}"

    for pointItem in dotList:
        dotArray[pointItem] = "1"
    
    logging.debug(f"\n{dotArray}")

    return (dotArray, foldInstructionList)
    
def processInput(dotArray, foldInstructionList):

    # don't forget to reference global variables here if needed
    # ---
    
    for index, instructionItem in enumerate(foldInstructionList):
        logging.debug(f"{instructionItem = }")
        # this is counterintuitive because the visual representation of an array is rotated 90 degrees
        # so folding on the x axis is actually a row fold, and the y axis fold is a column fold
        # chop the array at the line
        if instructionItem['axis'] == 'x':
            # chop at row x
            for column in range(dotArray.shape[1]):
                dotArray[(instructionItem['value'], column)] = instructionItem['value']
            logging.debug(f"\n{dotArray}")
            dotArray1 = dotArray[:instructionItem['value'], :]
            dotArray2 = dotArray[instructionItem['value']+1:, :]
            logging.debug(f"\n{dotArray1}\n\n{dotArray2}")
            dotArray2Flipped = numpy.flipud(dotArray2)
            logging.debug(f"\nflipped\n{dotArray2Flipped}")
        elif instructionItem['axis'] == 'y':
            # chop at column y
            for row in range(dotArray.shape[0]):
                dotArray[(row, instructionItem['value'])] = instructionItem['value']
            logging.debug(f"\n{dotArray}")
            dotArray1 = dotArray[:,:instructionItem['value']]
            dotArray2 = dotArray[:,instructionItem['value']+1:]
            logging.debug(f"\n{dotArray1}\n\n{dotArray2}")
            dotArray2Flipped = numpy.fliplr(dotArray2)
            logging.debug(f"\nflipped\n{dotArray2Flipped}")
        else:
            assert False,  f"unknown dimension in instruction list: {instructionItem}"
        # reshape the second, assumed smaller, array to be the same size as the first, assumed larger, array
        biggerArrayShape = dotArray1.shape
        smallerArrayShape = dotArray2.shape
        # differenceShape = biggerArrayShape - smallerArrayShape
        differenceShape = tuple(map(sub, biggerArrayShape, smallerArrayShape))
        axisZeroPad = differenceShape[0]
        axisOnePad = differenceShape[1]
        # https://stackoverflow.com/questions/9251635/python-resize-an-existing-array-and-fill-with-zeros
        dotArray2Flipped = numpy.pad(dotArray2Flipped, ((0,axisZeroPad), (0,axisOnePad)) )
        dotArray = dotArray1 | dotArray2Flipped
        logging.debug(f"\n{dotArray}")

    return(dotArray)

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

    dotArray, foldInstructionList = separateInput(inputList)

    answer = processInput(dotArray, foldInstructionList)

    if unitTesting:
        testPass = False

        # write the assignment of a boolean here that will determine if the unit test passed or not
        testPass = (False) # for part 2 we can't have a unit test because we are looking for eight character

        print("testPass:", testPass)
    else:
        # print the answer here
        print(numpy.transpose(answer))

    # this answer for my input is LGHEGUEJ

    endTime = time.perf_counter() # time in seconds (float)

    if timing:
        logging.info(f"Execution took {endTime - startTime} seconds.")

if __name__ == '__main__':
    main()
