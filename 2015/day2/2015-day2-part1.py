# Advent of Code - 2015 - Day 2

import os

# cwd = os.getcwd()  # Get the current working directory (cwd)
# files = os.listdir(cwd)  # Get all the files in that directory
# print("Files in %r: %s" % (cwd, files))

DEBUG = False

# read the input text file into a variable called presents
with open("2015/day2/input.txt","r") as inputString:
    presents = inputString.readlines()

# print(presents)

# define a new list of dictionaries called presents2
presents2 = []

# loop through presents (text input file) and decode each line into the length, width, and height for each present ("l","w","h")
# note we are using 'replace' on the third element of the temporary list of dimensions to get rid of the newline character
# TODO is this necessary if we cast to an integer later?
# and we are casting the string to an integer so we can do math
for present in presents:
    as_list = present.split("x")
    # print(as_list[2])
    as_list[2] = as_list[2].replace("\n","")
    presents2.append({"l":int(as_list[0]),"w":int(as_list[1]),"h":int(as_list[2])})
    # print(as_list)

# print the third present just as a debug check
if DEBUG == True:
    print(presents2[2])

grandTotal = 0

# go through the list of presents and calculate the total area of wrapping paper for each
for present in presents2:
    # print(present)
    # calculate the side areas
    sides = [present["l"]*present["w"], present["w"] * present["h"], present["h"] * present["l"]]
    # add up the sides
    area = 2 * sides[0] + 2 * sides[1] + 2 * sides[2]
    totalNeeded = area  + min(sides)
    present["totalNeeded"] = totalNeeded
    # print(totalNeeded)
    grandTotal += totalNeeded

if DEBUG == True:
    print(presents2[2])

print(grandTotal)