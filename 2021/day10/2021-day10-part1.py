# Advent of Code - 2021 - Day 10

# https://adventofcode.com/2021/day/10


import time, math, logging, os
from types import SimpleNamespace


def readInput(inputTextFileName):
    # global inputList

    with open(inputTextFileName,"r", encoding='utf-8') as file:
        inputList = file.readlines()

    # remove newlines
    inputList = [listItem.rstrip() for listItem in inputList]
    
    return(inputList)

def processInput(inputList):

    scoreDict = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }

    chunkList = ['()', '[]', '{}', '<>']
    closingCharList = [')', ']', '}', '>']
    corruptLinesList = []

    # don't forget to reference global variables here if needed
    # ---

    score = 0
    # tallyDict = {
    #     '(': 0,
    #     '[': 0,
    #     '{': 0,
    #     '<': 0,
    #     ')': 0,
    #     ']': 0,
    #     '}': 0,
    #     '>': 0
    # }

    # new idea -- go through each line with smallest chunks, remove them from the string until there are no more matching chunks
    # then the first closing character we find means it's a corrupt string, log that score

    for listItem in inputList:
        logging.debug(f"listItem: {listItem}")
        # loop through this listItem until there are not simple chunks left
        simpleChunksLeft = True
        testString = listItem
        while simpleChunksLeft:
            for chunk in chunkList:
                while chunk in testString:
                    # found the chunk, remove it
                    logging.debug(f"chunk: {chunk} testString: {testString}")
                    testString = testString.replace(chunk,'')
            # at this point we've iterated through the chunk list and removed every instance from the string
            # however, that removal may have created new instances of simple chunks, so we need to test for that and keep looping
            if any(chunk in testString for chunk in chunkList):
                simpleChunksLeft = True
            else:
                simpleChunksLeft = False
        
        logging.debug(f"testString: {testString}")
        # now we should have removed all the simple chunks, and any possible instances of simple chunks
        for chunk in chunkList:
            assert chunk not in testString, f"error: chunk {chunk} still in testString {testString}"
        
        # only test for a corrupt line if one of the closing characters is in the line
        # otherwise maybe it's just an incomplete line
        if any(closingChar in testString for closingChar in closingCharList):
            corruptLinesList.append(listItem)
            # is the last charater left the corrupt on?
            charPositionDict = {
                ')': math.inf,
                ']': math.inf,
                '}': math.inf,
                '>': math.inf
            }
            for closingChar in closingCharList:
                if closingChar in testString:
                    # the order matters, we need to find the first closing character
                    logging.debug(f"found {closingChar} in string at position {testString.find(closingChar)} -- this is a corrupt line")
                    charPositionDict[closingChar] = testString.find(closingChar)

            logging.debug(f"charPositionDict: {charPositionDict}")
            # we now have a dictionary of positions of the closing characters in the teststring
            # the lowest one (the first one) is the one we want to score
            # firstClosingChar = min(charPositionDict.values())
            firstClosingChar = min(charPositionDict,key=charPositionDict.get)
            logging.debug(f"lowest position: {firstClosingChar}")
            score += scoreDict[firstClosingChar]

    logging.debug(f"corruptLinesList: {corruptLinesList}")

    return(score)

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

    score = processInput(inputList)

    logging.debug(f"score: {score}")
    if unitTesting:
        testPass = False

        # write the assignment of a boolean here that will determine if the unit test passed or not
        # logging.debug("Don't forget to update your unit test here.")
        testPass = (score == 26397)

        print("testPass:", testPass)
    else:
        # print the answer here
        # logging.debug("Don't forget to update your print statement of the output here.")
        print(score)

    # this answer for my input is 319233

    endTime = time.perf_counter() # time in seconds (float)

    if timing:
        logging.info(f"Execution took {endTime - startTime} seconds.")

if __name__ == '__main__':
    main()
