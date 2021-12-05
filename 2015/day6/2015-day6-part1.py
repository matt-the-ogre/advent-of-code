# Advent of Code - 2015 - Day 6

# --- Day 6: Probably a Fire Hazard ---
# Because your neighbors keep defeating you in the holiday house decorating contest year after year, you've decided to deploy one million lights in a 1000x1000 grid.

# Furthermore, because you've been especially nice this year, Santa has mailed you instructions on how to display the ideal lighting configuration.

# Lights in your grid are numbered from 0 to 999 in each direction; the lights at each corner are at 0,0, 0,999, 999,999, and 999,0. The instructions include whether to turn on, turn off, or toggle various inclusive ranges given as coordinate pairs. Each coordinate pair represents opposite corners of a rectangle, inclusive; a coordinate pair like 0,0 through 2,2 therefore refers to 9 lights in a 3x3 square. The lights all start turned off.

# To defeat your neighbors this year, all you have to do is set up your lights by doing the instructions Santa sent you in order.

# For example:

# turn on 0,0 through 999,999 would turn on (or leave on) every light.
# toggle 0,0 through 999,0 would toggle the first line of 1000 lights, turning off the ones that were on, and turning on the ones that were off.
# turn off 499,499 through 500,500 would turn off (or leave off) the middle four lights.
# After following the instructions, how many lights are lit?
import time

def doInstruction(instructionString):
    global grid
    # figure out the command - text to the first string
    # note I'm cheating a bit here because I massaged the input to remove the word "turn" from the "turn off" and "turn on" commands to make parsing easier

    # this alternate way of doing it would work with the original input
    # just need some logic to parse the elements of the created list
    # left as an exercise for the reader :-)
    alternateCommandString = instructionString.split(" ")
    if debug:
        print(alternateCommandString)
        
    commandString = instructionString[0 : instructionString.find(" ")]
    if debug:
        print(commandString)

    # remove command from instruction
    instructionString = instructionString[instructionString.find(" ") + 1 : ]
    if debug:
        print(instruction)

    # first range
    firstRangeString = instructionString[0 : instructionString.find(" ")]
    if debug:
        print(firstRangeString)

    # remove first range from instruction to get second range
    secondRangeString = instructionString[instructionString.find("through") + 8 : ]
    if debug:
        print(secondRangeString)

    # convert range strings to lists
    firstRangeList = [0,0]
    firstRangeList[0] = int(firstRangeString[0:firstRangeString.find(",")])
    firstRangeList[1] = int(firstRangeString[firstRangeString.find(",") + 1 : ])
    if debug:
        print(firstRangeList)

    secondRangeList = [0,0]
    secondRangeList[0] = int(secondRangeString[0:secondRangeString.find(",")])
    secondRangeList[1] = int(secondRangeString[secondRangeString.find(",") + 1 : ])
    if debug:
        print(secondRangeList)

    if debug:
        print(commandString,firstRangeList,secondRangeList)

    if commandString == "toggle":
        for x in range(firstRangeList[0],secondRangeList[0] + 1):
            for y in range(firstRangeList[1],secondRangeList[1] + 1):
                grid[x][y] = not grid[x][y]
                # if debug:
                #     print("Toggling",x,y)
    elif commandString == "off":
        for x in range(firstRangeList[0],secondRangeList[0] + 1):
            for y in range(firstRangeList[1],secondRangeList[1] + 1):
                grid[x][y] = False 
    elif commandString == "on":
        for x in range(firstRangeList[0],secondRangeList[0] + 1):
            for y in range(firstRangeList[1],secondRangeList[1] + 1):
                grid[x][y] = True
    else:
        print("Error: invalid command", commandString)

def makeGrid(width,height):
    global grid
    grid = [False] * width
    for x in range (width):
        grid[x] = [False] * height

startTime = time.perf_counter() # time in seconds (float)

debug = False
timing = True
unitTesting = False

litLightsCount = 0

grid = []

# unit tests, kind of

if unitTesting:
    print("Unit Testing")
    makeGrid(10,10)
    # if debug:
    #     print(grid)
    lightsInstructions = ["toggle 0,0 through 2,2", "off 1,1 through 2,2", "on 8,8 through 9,9"]
    for instruction in lightsInstructions:
        doInstruction(instruction)
else:
    # read the input text file into a variable called presents
    with open("2015/day6/input.txt","r") as inputString:
        lightsInstructions = inputString.readlines()

    # remove newlines
    for i in range(0, len(lightsInstructions)):
        lightsInstructions[i] = lightsInstructions[i].rstrip()

    makeGrid(1000,1000)

    for instruction in lightsInstructions:
        doInstruction(instruction)

if debug:
    print(grid)

# count the lit lights
for row in grid:
    for cell in row:
        if cell:
            litLightsCount += 1

print(litLightsCount)

# the correct answer for my input is 543903

endTime = time.perf_counter() # time in seconds (float)

if timing:
    print("Execution took ", endTime - startTime, " seconds.")

