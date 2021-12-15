# Advent of Code - 2021 - Day 8

# https://adventofcode.com/2021/day/8


import time, math, logging ,os
from types import prepare_class


def readInput(inputTextFileName):
    # global inputList

    with open(inputTextFileName,"r", encoding='utf-8') as file:
        inputList = file.readlines()

    # remove newlines
    inputList = [listItem.rstrip() for listItem in inputList]

    inputList = [listItem.split(' | ') for listItem in inputList]

    # split the space-delimited strings into lists of strings
    for lineIndex, lineList in enumerate(inputList):
        inputList[lineIndex][0] = lineList[0].split(' ')
        inputList[lineIndex][1] = lineList[1].split(' ')
        # now sort the individual characters of each string to alphabetical order
        inputList[lineIndex][0] = [''.join(sorted(listItem)) for listItem in inputList[lineIndex][0]]
        inputList[lineIndex][1] = [''.join(sorted(listItem)) for listItem in inputList[lineIndex][1]]
        logging.debug(f"lineList: {lineList}")
    

    return(inputList)

def check_text(text, name):
    if all(x in name for x in text):
        char_index = [name.index(x) for x in text]
        return char_index == sorted(char_index)
    else:
        return False

def processInput(inputList):

    # don't forget to reference global variables here if needed
    # ---
    uniqueDigitsCount = 0
    outputDigitSum = 0

    # let's build a dictionary of segments to numbers
    # start with the unique ones we can determine
    for inputLineList, outputLineList in inputList:
        segmentToNumberDict = {}
        numberToSegmentDict = {}
        logging.debug(f"new line: {inputLineList}")
        # go through the input list and identify the unique digits and put them in dictionaries
        for inputDigit in inputLineList:
            if len(inputDigit) == 2:
                # digit 1
                segmentToNumberDict[inputDigit] = 1
                numberToSegmentDict[1] = inputDigit
                # uniqueDigitsCount += 1
            elif len(inputDigit) == 3:
                # digit 7
                segmentToNumberDict[inputDigit] = 7
                numberToSegmentDict[7] = inputDigit
            elif len(inputDigit) == 4:
                # digit 4
                segmentToNumberDict[inputDigit] = 4
                numberToSegmentDict[4] = inputDigit
            elif len(inputDigit) == 7:
                # digit 8
                segmentToNumberDict[inputDigit] = 8
                numberToSegmentDict[8] = inputDigit
        logging.debug(f"segmentToNumberDict: {segmentToNumberDict}")
        logging.debug(f"numberToSegmentDict: {numberToSegmentDict}")

        # I'm pretty sure we can remove the found items from the input list now
        logging.debug(f"inputLineList: {inputLineList}")
        inputLineList.remove(numberToSegmentDict[1])
        inputLineList.remove(numberToSegmentDict[4])
        inputLineList.remove(numberToSegmentDict[7])
        inputLineList.remove(numberToSegmentDict[8])
        logging.debug(f"inputLineList: {inputLineList}")

        # we have the unique digits in the dictionaries now
        # can we deduce the other digits from these?
        for inputDigit in inputLineList:
            if len(inputDigit) == 5:
                logging.debug(f"{inputDigit} length 5, can only be 2, 3, or 5")
                # digit 2, 3, or 5
                # if there is a '1' in this digit then it's a three by default
                if check_text(numberToSegmentDict[1],inputDigit):
                    logging.debug(f"this is a three: {inputDigit} because it contains: {numberToSegmentDict[1]}")
                    segmentToNumberDict[inputDigit] = 3
                    numberToSegmentDict[3] = inputDigit
            elif len(inputDigit) == 6:
                logging.debug(f"{inputDigit} is length 6, can only be 0, 6, or 9")
                # digit 0, 6, or 9
                # if there is a '4' in this digit then it's a nine by default
                if check_text(numberToSegmentDict[4], inputDigit):
                    logging.debug(f"this is a nine: {inputDigit} because it contains: {numberToSegmentDict[4]}")
                    segmentToNumberDict[inputDigit] = 9
                    numberToSegmentDict[9] = inputDigit
                # if there is a 1 in this digit then it's a zero by default
                elif check_text(numberToSegmentDict[1], inputDigit):
                    logging.debug(f"this is a zero: {inputDigit} because it contains: {numberToSegmentDict[1]}")
                    segmentToNumberDict[inputDigit] = 0
                    numberToSegmentDict[0] = inputDigit
                # else can only be a six
                else:
                    logging.debug(f"this is a six: {inputDigit} by default")
                    segmentToNumberDict[inputDigit] = 6
                    numberToSegmentDict[6] = inputDigit
        logging.debug(f"segmentToNumberDict: {segmentToNumberDict}")
        logging.debug(f"numberToSegmentDict: {numberToSegmentDict}")
        
        logging.debug(f"inputLineList: {inputLineList}")
        inputLineList.remove(numberToSegmentDict[0])
        inputLineList.remove(numberToSegmentDict[3])
        inputLineList.remove(numberToSegmentDict[6])
        inputLineList.remove(numberToSegmentDict[9])
        logging.debug(f"inputLineList: {inputLineList}")

        # one last round to deduce 2 or 5 using 6 and 9, but the reverse
        # as in: test if the digit in question is in six, then it's a five
        # and test if the digit in question is in nine then it's a two
        # we have the unique digits in the dictionaries now
        # can we deduce the other digits from these?
        for inputDigit in inputLineList:
            # digit 2, or 5
            if check_text(inputDigit,numberToSegmentDict[6]):
                logging.debug(f"this is a five: {inputDigit} because it is contained in: {numberToSegmentDict[6]}")
                segmentToNumberDict[inputDigit] = 5
                numberToSegmentDict[5] = inputDigit
            else:
                # only thing left is a two
                logging.debug(f"this is a two: {inputDigit} by default")
                segmentToNumberDict[inputDigit] = 2
                numberToSegmentDict[2] = inputDigit

        assert len(segmentToNumberDict) == 10, "wrong length of segmentToNumberDict, should be 10"
        assert len(numberToSegmentDict) == 10, "wrong length of numberToSegmentDict, should be 10"
        logging.debug(f"segmentToNumberDict: {segmentToNumberDict}")
        logging.debug(f"numberToSegmentDict: {numberToSegmentDict}")

        # okay, we have a dictionary, so we can decode the output digits
        thisDigitSum = 0
        for position, digit in enumerate(outputLineList):
            thisDigit = segmentToNumberDict[digit]
            thisDigitSum += 10**(3-position)*thisDigit
            logging.debug(f"position: {position} digit: {digit} thisDigit: {thisDigit} thisDigitSum: {thisDigitSum}")
        outputDigitSum += thisDigitSum


    return(outputDigitSum)

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

    answer = processInput(inputList)

    logging.debug(f"answer: {answer}")

    if unitTesting:
        testPass = False

        # write the assignment of a boolean here that will determine if the unit test passed or not
        # logging.info("Don't forget to update your unit test here.")
        testPass = (answer == 61229)

        print("testPass:", testPass)
    else:
        # print the answer here
        # logging.info("Don't forget to update your print statement of the output here.")
        print(answer)

    # this answer for my input is 

    endTime = time.perf_counter() # time in seconds (float)

    if timing:
        logging.info(f"Execution took {endTime - startTime} seconds.")

if __name__ == '__main__':
    main()
