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

# Your puzzle answer was 238.

# --- Part Two ---

# Realizing the error of his ways, Santa has switched to a better model of determining whether a string is naughty or nice. None of the old rules apply, as they are all clearly ridiculous.

# Now, a nice string is one with all of the following properties:

# It contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
# It contains at least one letter which repeats with exactly one letter between them, like xyx, abcdefeghi (efe), or even aaa.
# For example:

# qjhvhtzxzqqjkmpb is nice because is has a pair that appears twice (qj) and a letter that repeats with exactly one letter between them (zxz).
# xxyxx is nice because it has a pair that appears twice and a letter that repeats with one between, even though the letters used by each rule overlap.
# uurcxstgmygtbstg is naughty because it has a pair (tg) but no repeat with a single letter between them.
# ieodomkazucvgmuy is naughty because it has a repeating letter with one between (odo), but no pair that appears twice.

# How many strings are nice under these new rules?

import time

def hasTwoLetterPair(stringToTest):
    # let's go through the string with each possible pair (26 x 2) options to see if it has two pairs
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

    # test for a pair of any two letters that appears twice in the string without overlapping
    countPairs = 0
    for firstLetter in alphabet:
        for secondLetter in alphabet:
            pairOfLetters = firstLetter + secondLetter
            pairPosition = stringToTest.find(pairOfLetters)
            if pairPosition != -1:
                if debug:
                    print("Found pair ", pairOfLetters, " in string at position ", pairPosition)
                    print("testing substring: ", stringToTest[pairPosition+2:])
                pairPosition = stringToTest[pairPosition+2:].find(pairOfLetters)
                if pairPosition != -1:
                    if debug:
                        print("Found a second pair in string at new position ", pairPosition)
                    countPairs += 1
    
    if countPairs > 0:
        return True
    else:
        return False

def hasTwoLetterRepeat(stringToTest):
    # what if I created a dictionary for each string that tracks the position each letter appears in the string?
    # {"a":[0,3,6]} etc.
    # then I can walk each list and look for positions that are off by two
    # as soon as I find one I can break out of the loop

    # step 1 - make the dictionary

    letterPositions = {}
    for currentLetter in stringToTest:
        letterPositions.update({currentLetter : []})

    # step 2 - loop through the string and populate the dictionary with every position each letter appears in

    currentPosition = 0

    for currentLetter in stringToTest:
        if debug:
            print("finding letter", currentLetter)

        foundPosition = stringToTest.find(currentLetter, currentPosition)
        if debug:
            print("found position", foundPosition)

        tempList = letterPositions[currentLetter]
        tempList.append(foundPosition)
        letterPositions[currentLetter] = tempList
        currentPosition = foundPosition+1
    
    if debug:
        print(letterPositions)
    
    # found a case that didn't work -- "aaaa" should be nice
    # need to test all pairs in the position list for a delta of two spots
    # not just adjacent pairs
    # fixed in this version

    for currentLetter in letterPositions:
        positionList = letterPositions[currentLetter]
        for i in range(0,len(positionList)):
            for j in range(i+1,len(positionList)):
                if positionList[j] - positionList[i] == 2:
                # found a repeated letter with exactly one letter between
                    if debug:
                        print("Found repeated letter", currentLetter, "at positions", positionList[i], "and", positionList[i+1])
                    return True
    
    # didn't find a repeated letter exactly one letter apart
    return False

def niceString(stringToTest):
    if debug:
        print(stringToTest)
    
    if hasTwoLetterPair(stringToTest):
        # all good keep going
        if debug:
            print("Passed first test")
        if hasTwoLetterRepeat(stringToTest):
            if debug:
                print("Passed second test")
            return True 
    return False # string is naughty

startTime = time.time() # time in seconds (float)

debug = False
unitTesting = False

# unit tests, kind of

if unitTesting:
    testString = "xyxy"
    print("Test ", testString, "should be Nice. ", niceString(testString))
    testString = "aabcdefgaa"
    print("Test ", testString, "should be Naughty. ", niceString(testString) == False)
    testString = "aaa"
    print("Test ", testString, "should be Naughty. ", niceString(testString) == False)
    testString = "qjhvhtzxzqqjkmpb"
    print("Test ", testString, "should be Nice. ", niceString(testString))
    testString = "xxyxx"
    print("Test ", testString, "should be Nice. ", niceString(testString))
    testString = "aaaa"
    print("Test ", testString, "should be Nice. ", niceString(testString))
    testString = "uurcxstgmygtbstg"
    print("Test ", testString, "should be Naughty. ", niceString(testString) == False)
    testString = "ieodomkazucvgmuy"
    print("Test ", testString, "should be Naughty. ", niceString(testString) == False)


niceStringsCount = 0

if unitTesting == False:
    # read the input text file into a variable called presents
    with open("2015/day5/input.txt","r") as inputString:
        santaStrings = inputString.readlines()

    # remove newlines and count nice strings
    for i in range(0, len(santaStrings)):
        santaStrings[i] = santaStrings[i].rstrip()
        if niceString(santaStrings[i]):
            niceStringsCount += 1

    if debug:
        print("Total strings: ", len(santaStrings))

    print(niceStringsCount)

# 69 is the right answer for my input text

endTime = time.time() # time in seconds (float)

if debug:
    print("Execution took ", endTime - startTime, " seconds.")