# Advent of Code - 2021 - Day 6

# https://adventofcode.com/2021/day/6


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

    for index, item in enumerate(inputList):
        inputList[index] = int(item)

    logging.debug(f"inputList: {inputList}")

    return(inputList)

def processInput(inputList):

    # don't forget to reference global variables here if needed
    # ---

    newList = []

    for listItem in inputList:
        if listItem == 0:
            # new fish
            newList.append(6) # same fish restarts its reproductive timer
            newList.append(8) # new fish starts with 8 days to reproduce
        else:
            newList.append(listItem - 1)
        pass

    return(newList)

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
    numberOfDays = 80
    # ---
    
    if unitTesting:
        logging.info("Unit Testing")
        inputList = readInput(f"{filepath}/unit-test-input.txt")
    else:
        # read the input text file into a variable
        inputList = readInput(f"{filepath}/input.txt")

    while numberOfDays > 0:
        inputList = processInput(inputList)
        if numberOfDays == (80-17):
            logging.debug(f"number of fish on day 18: {len(inputList)}")
        elif numberOfDays == 1:
            logging.debug(f"number of fish on day 80: {len(inputList)}")
        numberOfDays -= 1


    answer = len(inputList)

    logging.debug(f"answer: {answer}")

    if unitTesting:
        testPass = False

        # write the assignment of a boolean here that will determine if the unit test passed or not
        # logging.debug("Don't forget to update your unit test here.")
        testPass = (answer == 5934)

        print("testPass:", testPass)
    else:
        # print the answer here
        # logging.debug("Don't forget to update your print statement of the output here.")
        print(answer)

    # this answer for my input is 

    endTime = time.perf_counter() # time in seconds (float)

    if timing:
        logging.info(f"Execution took {endTime - startTime} seconds.")

if __name__ == '__main__':
    main()
