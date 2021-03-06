# Advent of Code - 2021 - Day 4

# https://adventofcode.com/2021/day/4

# --- Day 4: Giant Squid ---

# You're already almost 1.5km (almost a mile) below the surface of the ocean, already so deep that you can't see any sunlight. What you can see, however, is a giant squid that has attached itself to the outside of your submarine.

# Maybe it wants to play bingo?

# Bingo is played on a set of boards each consisting of a 5x5 grid of numbers. Numbers are chosen at random, and the chosen number is marked on all boards on which it appears. (Numbers may not appear on all boards.) If all numbers in any row or any column of a board are marked, that board wins. (Diagonals don't count.)

# The submarine has a bingo subsystem to help passengers (currently, you and the giant squid) pass the time. It automatically generates a random order in which to draw numbers and a random set of boards (your puzzle input). For example:

# 7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

# 22 13 17 11  0
#  8  2 23  4 24
# 21  9 14 16  7
#  6 10  3 18  5
#  1 12 20 15 19

#  3 15  0  2 22
#  9 18 13 17  5
# 19  8  7 25 23
# 20 11 10 24  4
# 14 21 16 12  6

# 14 21 17 24  4
# 10 16 15  9 19
# 18  8 23 26 20
# 22 11 13  6  5
#  2  0 12  3  7

# After the first five numbers are drawn (7, 4, 9, 5, and 11), there are no winners, but the boards are marked as follows (shown here adjacent to each other to save space):

# 22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
#  8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
# 21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
#  6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
#  1 12 20 15 19        14 21 16 12  6         2  0 12  3  7

# After the next six numbers are drawn (17, 23, 2, 0, 14, and 21), there are still no winners:

# 22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
#  8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
# 21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
#  6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
#  1 12 20 15 19        14 21 16 12  6         2  0 12  3  7

# Finally, 24 is drawn:

# 22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
#  8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
# 21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
#  6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
#  1 12 20 15 19        14 21 16 12  6         2  0 12  3  7

# At this point, the third board wins because it has at least one complete row or column of marked numbers (in this case, the entire top row is marked: 14 21 17 24 4).

# The score of the winning board can now be calculated. Start by finding the sum of all unmarked numbers on that board; in this case, the sum is 188. Then, multiply that sum by the number that was just called when the board won, 24, to get the final score, 188 * 24 = 4512.

# To guarantee victory against the giant squid, figure out which board will win first. What will your final score be if you choose that board?

import time, math, logging

startTime = time.perf_counter() # time in seconds (float)

debug = False
level = logging.DEBUG
# level = logging.ERROR
fmt = '[%(levelname)s] %(asctime)s - %(message)s'
logging.basicConfig(level=level, format=fmt)
timing = True
unitTesting = False
inputList = []

# day-specific variables go here
numbersDrawnList = []
bingoBoardsList = []
# I'm going to hard code a few variables for ease
BOARD_COLUMNS = 5
BOARD_ROWS = 5

class Board:
    def __init__(self, boardList):
        self.board = []
        self.winner = False
        self.score = 0
        for line in boardList:
            boardLine = []
            for item in line:
                # be sure to convert to integer because they might be coming in as strings
                boardLine.append({"number": int(item), "marked": False})
            self.board.append(boardLine)
        logging.debug(self.board)

    def __str__(self):
        returnString = ""
        for line in self.board:
            returnString += "| "
            for item in line:
                number = item["number"]
                if item["marked"]:
                    returnString += f" *{number}* "
                else:
                    returnString += f" {number} "
            returnString += " |\n"
        return(returnString)

    def markNumber(self, number):
        for line in self.board:
            for item in line:
                if item["number"] == number:
                    item["marked"] = True

    def checkWinner(self):
        # check rows for five marked numbers
        for line in self.board:
            markedCount = 0
            for item in line:
                if item["marked"]:
                    markedCount += 1
            if markedCount == 5:
                return True
        # now check columns
        for i in range(0,BOARD_ROWS):
            markedCount = 0
            for line in self.board:
                if line[i]["marked"]:
                    markedCount += 1
            if markedCount == 5:
                return True
        return False

    def boardScore(self,numberCalled):
        self.score = 0
        for line in self.board:
            for item in line:
                if item["marked"] is False:
                    # add it to the score
                    self.score += item["number"]
        self.score *= numberCalled
        return(self.score)

# I'm thinking we have a 2d board as a list of lists of dictionaries
# testBoardList = [
#     [22, 13, 17, 11,  0],
#     [8,  2, 23,  4, 24],
#     [21,  9, 14, 16,  7],
#     [6, 10,  3, 18,  5],
#     [1, 12, 20, 15, 19]
#     ]

# testBoard = Board(testBoardList)

# logging.debug(testBoard)
# logging.debug(testBoard.checkWinner())

# testBoard.markNumber(999)
# testBoard.markNumber(8)
# testBoard.markNumber(2)
# testBoard.markNumber(23)
# testBoard.markNumber(4)
# testBoard.markNumber(24)

# logging.debug(testBoard)
# logging.debug(testBoard.checkWinner())
# logging.debug(testBoard.boardScore(24))

# ---

def readInput(inputTextFileName):
    global inputList, numbersDrawnList, bingoBoardsList

    with open("2021/day4/"+inputTextFileName,"r", encoding='utf-8') as file:
        inputList = file.readlines()

    # remove newlines
    for i in range(0, len(inputList)):
        inputList[i] = inputList[i].rstrip()

    # first put the first line into the numbers drawn list
    numbersDrawnList = inputList[0].split(",")
    for i in range(0, len(numbersDrawnList)):
        numbersDrawnList[i] = int(numbersDrawnList[i])

    # then there's a newline so we start on line 2 (the third line) of the remaining input to start parsing boards
    # and we go by 6 lines because each board is five rows plus a blank line
    for inputLineNum in range(2,len(inputList),BOARD_ROWS + 1):
        tempBoardList = []
        for i in range(0,5):
            tempBoardList.append(inputList[inputLineNum+i].split())
        # note the tempBoardList is a list of strings
        # rather than convert to integers here I'm just casting as integers in the Board class init function
        # make a new Board object in the main boards list from the temp list we just parsed
        bingoBoardsList.append(Board(tempBoardList))
        # skip the blank line between boards in the input list (the step in the range)
    return()

def processInput():
    # don't forget to reference global variables here if needed
    global numbersDrawnList, bingoBoardsList, inputList
    # ---

    for numberDrawn in numbersDrawnList:
        for board in bingoBoardsList:
            board.markNumber(numberDrawn)
            if board.checkWinner():
                logging.debug("Winning numberDrawn:", numberDrawn)
                logging.debug("Winning board:", board)
                return(board.boardScore(numberDrawn))

    return(math.nan)

if unitTesting:
    logging.info("Unit Testing")
    readInput("unit-test-input.txt")
else:
    # read the input text file into a variable
    readInput("input.txt")

winningBoardScore = processInput()

logging.debug("winningBoardScore:", winningBoardScore)

if unitTesting:
    testPass = False

    # write the assignment of a boolean here that will determine if the unit test passed or not
    testPass = (winningBoardScore == 4512)

    print("testPass:", testPass)
else:
    # logging.debug the answer here
    print(winningBoardScore)

# this answer for my input is 29440

endTime = time.perf_counter() # time in seconds (float)

if timing:
    logging.info(f"Execution took {endTime - startTime} seconds.")

