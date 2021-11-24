# Advent of Code - 2015 - Day 4

# --- Day 4: The Ideal Stocking Stuffer ---
# Santa needs help mining some AdventCoins (very similar to bitcoins) to use as gifts for all the economically forward-thinking little girls and boys.

# To do this, he needs to find MD5 hashes which, in hexadecimal, start with at least five zeroes. The input to the MD5 hash is some secret key (your puzzle input, given below) followed by a number in decimal. To mine AdventCoins, you must find Santa the lowest positive number (no leading zeroes: 1, 2, 3, ...) that produces such a hash.

# For example:

# If your secret key is abcdef, the answer is 609043, because the MD5 hash of abcdef609043 starts with five zeroes (000001dbbfa...), and it is the lowest such number to do so.
# If your secret key is pqrstuv, the lowest number it combines with to make an MD5 hash starting with five zeroes is 1048970; that is, the MD5 hash of pqrstuv1048970 looks like 000006136ef....
# Your puzzle input is yzbqklnj.

import hashlib

puzzleInput = "yzbqklnj"

debug = False

# What to do here? Brute force?

# figure out how to do MD5 hashes of an arbitary string in Python
# write a function to check if an MD5 hash has five or more leading zeroes
# loop infinitely from 1 until condition is met

def fiveZeroes(stringToCheck):
    if debug:
        print("Checking ", stringToCheck)

    # do the md5 has on the string    
    md5_value = hashlib.md5(stringToCheck)

    if debug:
        print(md5_value.hexdigest())

    # check if the first five characters are zeroes
    if md5_value.hexdigest()[:5] == "00000":
        return True
    else:
        return False

# start with 1
i = 1

# loop until our function returns True
while fiveZeroes(str(puzzleInput+str(i)).encode('utf-8')) != True:
    # increment our counter
    i += 1
    if debug and (i%10 == 0):
        print(i)

# print the answer
print(i)
