# Advent of Code - 2021 - Day 2

# https://adventofcode.com/2021/day/2

# --- Day 2: Dive! ---

# Now, you need to figure out how to pilot this thing.

# It seems like the submarine can take a series of commands like forward 1, down 2, or up 3:

# forward X increases the horizontal position by X units.
# down X increases the depth by X units.
# up X decreases the depth by X units.
# Note that since you're on a submarine, down and up affect your depth, and so they have the opposite result of what you might expect.

# The submarine seems to already have a planned course (your puzzle input). You should probably figure out where it's going. For example:

# forward 5
# down 5
# forward 8
# up 3
# down 8
# forward 2

# Your horizontal position and depth both start at 0. The steps above would then modify them as follows:

# forward 5 adds 5 to your horizontal position, a total of 5.
# down 5 adds 5 to your depth, resulting in a value of 5.
# forward 8 adds 8 to your horizontal position, a total of 13.
# up 3 decreases your depth by 3, resulting in a value of 2.
# down 8 adds 8 to your depth, resulting in a value of 10.
# forward 2 adds 2 to your horizontal position, a total of 15.

# After following these instructions, you would have a horizontal position of 15 and a depth of 10. (Multiplying these together produces 150.)

# Calculate the horizontal position and depth you would have after following the planned course. What do you get if you multiply your final horizontal position by your final depth?

import time, math

startTime = time.perf_counter() # time in seconds (float)

debug = False
timing = False
unitTesting = False

depth = 0
horizontalPosition = 0

commandsList = []

def readInput(inputTextFileName):
    global commandsList

    with open("2021/day2/"+inputTextFileName,"r", encoding='utf-8') as file:
        commandsList = file.readlines()

    # remove newlines
    for i in range(0, len(commandsList)):
        commandsList[i] = commandsList[i].rstrip()

def doCommands():
    global commandsList
    global depth
    global horizontalPosition

    for command in commandsList:
        direction = command.split(" ")[0]
        amount = int(command.split(" ")[1])
        if debug:
            print("command:", command,"direction:",direction, "amount:", amount)
        if direction == "forward":
            horizontalPosition += amount
        elif direction == "up":
            depth -= amount
        elif direction == "down":
            depth += amount
        else:
            print("Unknown direction:", direction)
    return()

if unitTesting:
    print("Unit Testing")
    readInput("unit-test-input.txt")
else:
    # read the input text file into a variable
    readInput("input.txt")

doCommands()

if unitTesting:
    testPass = False

    testPass = (depth * horizontalPosition == 150)

    print("testPass:", testPass)
else:
    print(depth * horizontalPosition)

# this answer for my input is 1635930

endTime = time.perf_counter() # time in seconds (float)

if timing:
    print("Execution took ", endTime - startTime, " seconds.")

