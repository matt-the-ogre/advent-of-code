# Advent of Code - 2015 - Day 3

# https://adventofcode.com/2015/day/3

# --- Day 3: Perfectly Spherical Houses in a Vacuum ---
# Santa is delivering presents to an infinite two-dimensional grid of houses.

# He begins by delivering a present to the house at his starting location, and then an elf at the North Pole calls him via radio and tells him where to move next. Moves are always exactly one house to the north (^), south (v), east (>), or west (<). After each move, he delivers another present to the house at his new location.

# However, the elf back at the north pole has had a little too much eggnog, and so his directions are a little off, and Santa ends up visiting some houses more than once. How many houses receive at least one present?

# For example:

# > delivers presents to 2 houses: one at the starting location, and one to the east.
# ^>v< delivers presents to 4 houses in a square, including twice to the house at his starting/ending location.
# ^v^v^v^v^v delivers a bunch of presents to some very lucky children at only 2 houses.

# --- Part Two ---
# The next year, to speed up the process, Santa creates a robot version of himself, Robo-Santa, to deliver presents with him.

# Santa and Robo-Santa start at the same location (delivering two presents to the same starting house), then take turns moving based on instructions from the elf, who is eggnoggedly reading from the same script as the previous year.

# This year, how many houses receive at least one present?

# For example:

# ^v delivers presents to 3 houses, because Santa goes north, and then Robo-Santa goes south.
# ^>v< now delivers presents to 3 houses, and Santa and Robo-Santa end up back where they started.
# ^v^v^v^v^v now delivers presents to 11 houses, with Santa going one direction and Robo-Santa going the other.

# import os

# cwd = os.getcwd()  # Get the current working directory (cwd)
# files = os.listdir(cwd)  # Get all the files in that directory
# print("Files in %r: %s" % (cwd, files))

DEBUG = False

# read the input text file into a variable called presents
with open("2015/day3/input.txt","r") as inputString:
    moves = inputString.readlines()

if DEBUG:
    print(moves[0])

# walk the steps and build a matrix, adding one to the number of presents at the house at x,y each time Santa passes 
# or
# sparse matrix of some sort? Maybe there is a 'hash' of locations? Then just count the length of the array?
#
# i.e. "0x0" is location 1, "0x1" is location two, etc. need a seperator otherwise we'd get hash collisions, right?

# iterate over the steps string, character by character

# starting position is 0,0
x = 0
y = 0

# start with Santa moving, then Robo-Santa, and alternate
thisMove = "Santa"
SantaX = 0
SantaY = 0

RoboSantaX = 0
RoboSantaY = 0

# add the first house to the dictionary in position "0x0" with a value of 1 present
houses = {str(x)+"x"+str(y) : 1}

if DEBUG:
    print (houses)

# iterate through the characters (step) of the string moves[0] (note: have to index into moves because it's a dictionary as imported from the input text file)

for step in moves[0]:
    if DEBUG:
        print(thisMove,step)

    # set x and y based on whose move it is
    if thisMove == "Santa":
        x = SantaX
        y = SantaY
    elif thisMove == "RoboSanta":
        x = RoboSantaX
        y = RoboSantaY
    else:
        print("Error: unknown value for 'thisMove': ", thisMove)
    
    # based on the character of the step, increment or decrement x or y
    if step == "^":
        y += 1
    elif step == "v":
        y -= 1
    elif step == ">":
        x += 1
    elif step == "<":
        x -= 1
    else:
        print("Error: Unrecognized step type: ", step)
        break
    
    # set the position of Santa or RoboSanta based on the updated move
    if thisMove == "Santa":
        # store the current coordinates for Santa (for his next move)
        SantaX = x
        SantaY = y
        # switch to RoboSanta for the next iteration through the loop
        thisMove = "RoboSanta"
    elif thisMove == "RoboSanta":
        RoboSantaX = x
        RoboSantaY = y
        thisMove = "Santa"
    else:
        print("Error: unknow value for 'thisMove': ", thisMove)
    
    currentHouse = str(x)+"x"+str(y)

    if DEBUG:
        print(currentHouse)
    
    # if we've been to this house before, increment the number of presents
    # Note: the get() function let's us test if the dictionary has a value without generating an exception
    if houses.get(currentHouse) != None:
        houses[currentHouse] += 1
    else:
        # never been here before, add to the dictionary, and set it to one present
        houses[currentHouse] = 1
    
if DEBUG:
    print(houses)

# number of houses that received at least one present is the length of the houses dictionary
print(len(houses))
