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

# --- Part Two ---

# On the other hand, it might be wise to try a different strategy: let the giant squid win.

# You aren't sure how many bingo boards a giant squid could play at once, so rather than waste time counting its arms, the safe thing to do is to figure out which board will win last and choose that one. That way, no matter which boards it picks, it will win for sure.

# In the above example, the second board is the last to win, which happens after 13 is eventually called and its middle column is completely marked. If you were to keep playing until this point, the second board would have a sum of unmarked numbers equal to 148 for a final score of 148 * 13 = 1924.

# Figure out which board will win last. Once it wins, what would its final score be?

import time, math

startTime = time.perf_counter() # time in seconds (float)

debug = False
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
        # pre-calculate the score, without the number called, at init time
        for line in self.board:
            for item in line:
                # add it to the score
                self.score += item["number"]
        if debug:
        #     print(self.board)
            print("self.score:",self.score)
            pass

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
                if item["number"] == int(number):
                    item["marked"] = True
                    self.score -= int(number)

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
        # there's likely an optimization here
        # rather than re-calculating every time, what if we added / subtracted to the score every time a square was marked?
        # we would calculate the score on init, then subtract when marked
        # self.score *= numberCalled
        return(self.score * numberCalled)

# I'm thinking we have a 2d board as a list of lists of dictionaries
# if debug:
#     testBoardList = [
#         [22, 13, 17, 11,  0],
#         [8,  2, 23,  4, 24],
#         [21,  9, 14, 16,  7],
#         [6, 10,  3, 18,  5],
#         [1, 12, 20, 15, 19]
#         ]

#     testBoard = Board(testBoardList)

#     print(testBoard)
#     print(testBoard.checkWinner())

#     testBoard.markNumber(999)
#     testBoard.markNumber(8)
#     testBoard.markNumber(2)
#     testBoard.markNumber(23)
#     testBoard.markNumber(4)
#     testBoard.markNumber(24)

#     print(testBoard)
#     print(testBoard.checkWinner())
#     print(testBoard.boardScore(24))

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

def checkAllBoardsWinners():
    winnersCount = 0
    for board in bingoBoardsList:
        if board.checkWinner():
            winnersCount += 1
    return(winnersCount == len(bingoBoardsList))

def processInput():
    # don't forget to reference global variables here if needed
    global numbersDrawnList, bingoBoardsList, inputList
    # ---
    lastWinningNumber = math.nan
    lastWinningScore = math.nan

    for numberDrawn in numbersDrawnList:
        for board in bingoBoardsList:
            board.markNumber(numberDrawn)
            if board.checkWinner():
                if debug:
                    print("Winning numberDrawn:", numberDrawn)
                    print("Winning board:", board)
                lastWinningScore = board.boardScore(numberDrawn)
                lastWinningNumber = numberDrawn
                if checkAllBoardsWinners():
                    return(lastWinningNumber,lastWinningScore)

    return(math.nan,math.nan)

if unitTesting:
    print("Unit Testing")
    readInput("unit-test-input.txt")
else:
    # read the input text file into a variable
    readInput("input.txt")

(winningBoardNumber, winningBoardScore) = processInput()

if debug:
    print("winningBoardNumber", winningBoardNumber, "winningBoardScore:", winningBoardScore)

if unitTesting:
    testPass = False

    # write the assignment of a boolean here that will determine if the unit test passed or not
    testPass = (winningBoardScore == 1924)

    print("testPass:", testPass)
else:
    # print the answer here
    print(winningBoardScore)

# this answer for my input is 13884

endTime = time.perf_counter() # time in seconds (float)

if timing:
    print("Execution took ", endTime - startTime, " seconds.")

