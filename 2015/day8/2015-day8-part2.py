# Advent of Code - 2015 - Day 8

# --- Day 8: Matchsticks ---

# Space on the sleigh is limited this year, and so Santa will be bringing his list as a digital copy. He needs to know how much space it will take up when stored.

# It is common in many programming languages to provide a way to escape special characters in strings. For example, C, JavaScript, Perl, Python, and even PHP handle special characters in very similar ways.

# However, it is important to realize the difference between the number of characters in the code representation of the string literal and the number of characters in the in-memory string itself.

# For example:

# "" is 2 characters of code (the two double quotes), but the string contains zero characters.
# "abc" is 5 characters of code, but 3 characters in the string data.
# "aaa\"aaa" is 10 characters of code, but the string itself contains six "a" characters and a single, escaped quote character, for a total of 7 characters in the string data.
# "\x27" is 6 characters of code, but the string itself contains just one - an apostrophe ('), escaped using hexadecimal notation.

# Santa's list is a file that contains many double-quoted string literals, one on each line. The only escape sequences used are \\ (which represents a single backslash), \" (which represents a lone double-quote character), and \x plus two hexadecimal characters (which represents a single character with that ASCII code).

# Disregarding the whitespace in the file, what is the number of characters of code for string literals minus the number of characters in memory for the values of the strings in total for the entire file?

# For example, given the four strings above, the total number of characters of string code (2 + 5 + 10 + 6 = 23) minus the total number of characters in memory for string values (0 + 3 + 7 + 1 = 11) is 23 - 11 = 12.

import time, math, sys, re

startTime = time.perf_counter() # time in seconds (float)

debug = True
timing = True
unitTesting = False

stringsList = []

def readInput(inputTextFileName):
    global stringsList

    with open("2015/day8/"+inputTextFileName,"r", encoding='utf-8') as file:
        stringsList = file.readlines()

    # remove newlines
    for i in range(0, len(stringsList)):
        stringsList[i] = stringsList[i].rstrip()

def processStrings():
    global stringsList

    codeCharacters = 0
    memoryCharacters = 0
    encodedCharacters = 0

    for stringItem in stringsList:
        codeCharacters += len(stringItem)

        memoryCharacters += (len(eval(stringItem)))

        # if debug:
        #     print(stringItem,stringItem[1: -1],repr(stringItem),repr(stringItem[1 : -1]),len(stringItem),(len(eval(stringItem))),len(repr(stringItem))+4)

        newString = stringItem
        if debug:
            print("newString before replace:",newString)
        if debug:
            print(re.findall(r'\\x[0-9a-fA-F]+', newString))
        newString = newString[0]+newString[1:-1].replace(r'\\',r'\\\\')+newString[-1]
        newString = newString[0]+newString[1:-1].replace(r'\"',r'\\\"')+newString[-1]
        if debug:
            print(re.findall(r'\\x[0-9a-fA-F]+', newString))
        # newString = newString.replace(r'\x',r'\\x')
        # newString = re.sub(r'\\x[0-9a-fA-F]+', r'\\\x0f', newString)
        newString = newString[0]+r'\"'+newString[1:-1]+r'\"'+newString[-1]
        if debug:
            print("newString after replace:",newString)

        encodedCharacters += len(newString)

    if debug:
        print("codeCharacters:",codeCharacters,"memoryCharacters:",memoryCharacters, "encodedCharacters:", encodedCharacters)
    
    return (codeCharacters, memoryCharacters, encodedCharacters)

if unitTesting:
    print("Unit Testing")
    readInput("unit-test-input.txt")
else:
    # read the input text file into a variable
    readInput("input.txt")

(codeCharacters, memoryCharacters, encodedCharacters) = processStrings()

answer = encodedCharacters - codeCharacters

if unitTesting:
    testPass = False
    
    if debug:
        print("answer:", answer)

    testPass = (answer == 19)

    print("testPass:", testPass)
else:
    print(answer)

# this answer for my input is 1371

endTime = time.perf_counter() # time in seconds (float)

if timing:
    print("Execution took ", endTime - startTime, " seconds.")

