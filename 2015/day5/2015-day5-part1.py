# Advent of Code - 2015 - Day 5

# https://adventofcode.com/2015/day/5

# --- Day 5: Doesn't He Have Intern-Elves For This? ---

# Santa needs help figuring out which strings in his text file are naughty or nice.

# A nice string is one with all of the following properties:

# It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
# It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
# It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.
# For example:

# ugknbfddgicrmopn is nice because it has at least three vowels (u...i...o...), a double letter (...dd...), and none of the disallowed substrings.
# aaa is nice because it has at least three vowels and a double letter, even though the letters used by different rules overlap.
# jchzalrnumimnmhp is naughty because it has no double letter.
# haegwjzuvuyypxyu is naughty because it contains the string xy.
# dvszwmarrgswjxmb is naughty because it contains only one vowel.

# How many strings are nice?

import time

def hasDoubles(stringToTest):
    count = 0
    doubleLettersList = ["aa","bb","cc","dd","ee","ff","gg","hh","ii","jj","kk","ll","mm","nn","oo","pp","qq","rr","ss","tt","uu","vv","ww","xx","yy","zz"]

    # go through the string by letter, comparing that letter and the next to a string of all double letters
    for i in range(0,len(stringToTest)-1):
        # if debug:
        #     print("Testing string ", stringToTest, " at ", i, " = ", stringToTest[i:i+2])
        if stringToTest[i:i+2] in doubleLettersList:
            # if debug:
            #     print("String ", stringToTest, " has double letters ", stringToTest[i:i+2])
            return True
    
    # if we didn't find a double letter, return False
    return False

def countVowels(stringToCount):
    count = 0
    for letter in stringToCount:
        if (letter in "aeiou"):
            count += 1
    return count

def niceString(stringToTest):
    # if debug:
    #     print(stringToTest)
    
    # first test for the forbidden substrings
    if ("ab" in stringToTest) or ("cd" in stringToTest) or ("pq" in stringToTest) or ("xy" in stringToTest):
        # if debug:
        #     print("String ", stringToTest," is naughty because of forbidden letters.")
        return False
    # must have at least three vowels to be nice
    if (countVowels(stringToTest) < 3):
        # if debug:
        #     print("String ", stringToTest," is naughty because of too few vowels: ", countVowels(stringToTest))
        return False
    # if we made it here the string has three vowels
    # now test for double letters
    if (hasDoubles(stringToTest)):
        # string has double letters, return True
        return True
    else:
        # string doesn't have double letters, return False
        # if debug:
        #     print("String ", stringToTest," is naughty because of no double letters.")
        return False

startTime = time.perf_counter() # time in seconds (float)

debug = True

niceStringsCount = 0

# read the input text file into a variable called presents
with open("2015/day5/input.txt","r") as inputString:
    santaStrings = inputString.readlines()

# remove newlines and count nice strings
for i in range(0, len(santaStrings)):
    santaStrings[i] = santaStrings[i].rstrip()
    if niceString(santaStrings[i]):
        niceStringsCount += 1


# if debug:
#     print(santaStrings)
#     print(type(santaStrings))

if debug:
    print("Total strings: ", len(santaStrings))

print(niceStringsCount)

endTime = time.perf_counter() # time in seconds (float)

if debug:
    print("Execution took ", endTime - startTime, " seconds.")