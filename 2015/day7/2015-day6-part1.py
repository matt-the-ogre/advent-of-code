# Advent of Code - 2015 - Day 7

# --- Day 7: Some Assembly Required ---
# This year, Santa brought little Bobby Tables a set of wires and bitwise logic gates! Unfortunately, little Bobby is a little under the recommended age range, and he needs help assembling the circuit.

# Each wire has an identifier (some lowercase letters) and can carry a 16-bit signal (a number from 0 to 65535). A signal is provided to each wire by a gate, another wire, or some specific value. Each wire can only get a signal from one source, but can provide its signal to multiple destinations. A gate provides no signal until all of its inputs have a signal.

# The included instructions booklet describes how to connect the parts together: x AND y -> z means to connect wires x and y to an AND gate, and then connect its output to wire z.

# For example:

# 123 -> x means that the signal 123 is provided to wire x.
# x AND y -> z means that the bitwise AND of wire x and wire y is provided to wire z.
# p LSHIFT 2 -> q means that the value from wire p is left-shifted by 2 and then provided to wire q.
# NOT e -> f means that the bitwise complement of the value from wire e is provided to wire f.
# Other possible gates include OR (bitwise OR) and RSHIFT (right-shift). If, for some reason, you'd like to emulate the circuit instead, almost all programming languages (for example, C, JavaScript, or Python) provide operators for these gates.

# For example, here is a simple circuit:

# 123 -> x
# 456 -> y
# x AND y -> d
# x OR y -> e
# x LSHIFT 2 -> f
# y RSHIFT 2 -> g
# NOT x -> h
# NOT y -> i
# After it is run, these are the signals on the wires:

# d: 72
# e: 507
# f: 492
# g: 114
# h: 65412
# i: 65079
# x: 123
# y: 456
# In little Bobby's kit's instructions booklet (provided as your puzzle input), what signal is ultimately provided to wire a?

import time, math

def createCircuitDict():
    global circuitStrings
    global circuitDict

    for circuitLine in circuitStrings:
        leftSide = circuitLine[0 : circuitLine.find("->") - 1]
        # if debug:
        #     print("leftSide:", leftSide)
        rightSide = circuitLine[circuitLine.find("->") + 3 : ]
        # if debug:
        #     print("rightSide:", rightSide)
        # put a test in here that checks for duplicate lines with the same input
        # could also put a test in here that checks that all the input lines are define / calculated as each new line is added
        # eliminates the need for recursion?

        # check for numeric input string -- this is easy, just make it the output
        # should this be in the next function though?
        outputValue = math.nan
        if leftSide.isnumeric():
            leftSide = int(leftSide)
            outputValue = leftSide # simple -- the input to this wire is also it's output
        
        if debug:
            if circuitDict.get(rightSide) != None:
                print("Weird... dictionary key ", rightSide, "already exists. This shouldn't happen.")
        
        circuitDict[rightSide] = {"input" : leftSide, "output" : outputValue}

def evaluateInput(circuit, operator):
    global circuitDict
    # if debug:
    #     print(circuit, operator)

    # check left argument for circuit name or number
    inputWire1 = circuitDict[circuit]["input"][: circuitDict[circuit]["input"].find(operator) - 1]
    inputWire2 = circuitDict[circuit]["input"][circuitDict[circuit]["input"].find(operator) + len(operator) + 1 : ]
    # if debug:
    #     print(circuit, "=", inputWire1, operator, inputWire2)
    # look up the output of the inputWire
    if inputWire1.isnumeric():
        input1 = int(inputWire1)
    else:
        input1 = circuitDict[inputWire1]["output"]
        
    if inputWire2.isnumeric():
        input2 = int(inputWire2)
    else:
        input2 = circuitDict[inputWire2]["output"]

    if math.isnan(input1):
        # print("input wire 1 isn't calculated yet")
        pass
    elif math.isnan(input2):
        # print("input wire 2 isn't calculated yet")
        pass
    else:
        # do the bitwise complement on the input number and assign it to the output of this wire
        if operator == "AND":
            circuitDict[circuit]["output"] = input1 & input2
        elif operator == "OR":
            circuitDict[circuit]["output"] = input1 | input2
        elif operator == "LSHIFT":
            circuitDict[circuit]["output"] = input1 << input2
        elif operator == "RSHIFT":
            circuitDict[circuit]["output"] = input1 >> input2
        else:
            print("Unknown operator", operator)
    
        # check for rollunder 0
        if circuitDict[circuit]["output"] < 0:
            # if debug:
            #     print("result under zero, fix it")
            circuitDict[circuit]["output"] =  65535 + circuitDict[circuit]["output"]

def doConnection():
    global circuitDict
    unfinishedCount = len(circuitDict)
    lowCount = unfinishedCount

    while unfinishedCount != 0:
        unfinishedCount = len(circuitDict)
        if debug:
            print("lowCount", lowCount)
        for circuit in circuitDict:
            # if the output is not a number, evaluate the input
            if math.isnan(circuitDict[circuit]["output"]):
                # parse the left side
                # we can have NOT, AND, OR, LSHIFT, and RSHIFT as possible commands
                if "NOT" in circuitDict[circuit]["input"]:
                    # operation is logical NOT, invert the input line to be the output
                    inputWire1 = circuitDict[circuit]["input"][circuitDict[circuit]["input"].find("NOT")+4 : ]
                    # if debug:
                    #     print(circuit, "= NOT", inputWire1)
                    # look up the output of the inputWire
                    if inputWire1.isnumeric():
                        input1 = int(inputWire1)
                    else:
                        input1 = circuitDict[inputWire1]["output"]
            
                    if math.isnan(input1):
                        # print("input wire isn't calculated yet")
                        pass
                    else:
                        # do the bitwise complement on the input number and assign it to the output of this wire
                        circuitDict[circuit]["output"] = ~input1
                        # check for rollunder 0
                        if circuitDict[circuit]["output"] < 0:
                            # if debug:
                            #     print("result under zero, fix it")
                            circuitDict[circuit]["output"] =  65536 + circuitDict[circuit]["output"]
                elif "AND" in circuitDict[circuit]["input"]:
                    evaluateInput(circuit, "AND")
                elif "OR" in circuitDict[circuit]["input"]:
                    evaluateInput(circuit, "OR")
                elif "LSHIFT" in circuitDict[circuit]["input"]:
                    evaluateInput(circuit, "LSHIFT")
                elif "RSHIFT" in circuitDict[circuit]["input"]:
                    evaluateInput(circuit, "RSHIFT")
                else:
                    # simplest case -- one input only!
                    # copy the input wire
                    # this could be improved by doing it only if the inputWire is resolved
                    inputWire1 = circuitDict[circuit]["input"]
                    if debug:
                        print("simplest case circuit", circuit, " inputWire", inputWire1)
                    circuitDict[circuit]["output"] = circuitDict[inputWire1]["output"]
            else:
                # this circuit is done, move on
                # if debug:
                #     print("circuit",circuit,"is done with output ", circuitDict[circuit]["output"], "Break.")
                pass
            if math.isnan(circuitDict[circuit]["output"]) == False:
                # this output is calculated, decrement the unfinished counter
                unfinishedCount -= 1
                if unfinishedCount < lowCount:
                    lowCount = unfinishedCount
                # if debug:
                #     print("unfinishedCount", unfinishedCount)

startTime = time.time() # time in seconds (float)

debug = False
timing = True
unitTesting = False

# maybe a dictionary again?
# circuitStrings = {"a" : {"input" : 1, "output" : NaN}}
# parse the input text file to set up the circuitStrings inputs, then just roll through the dictionary to calculate the outputs
# how will I be sure that the output has been calculated to be the input for the next circuitStrings? 
# can I assume the input file is "in order"? Probably not.
# does this mean some sort of recursion algorithm?
# maybe if I populate the outputs with 'NaN' (or Python equivalent) then check that it's not that before using it's output
# I can make it recurse through the inputs, calculating any that have fully realized inputs?

circuitStrings = []
circuitDict = {}

# unit tests, kind of

if unitTesting:
    print("Unit Testing")
    circuitStrings = ["123 -> x","456 -> y", "x AND y -> d", "x OR y -> e", "x LSHIFT 2 -> f", "y RSHIFT 2 -> g", "NOT x -> h", "NOT y -> i"]
else:
    # read the input text file into a variable called presents
    with open("2015/day7/input.txt","r") as inputString:
        circuitStrings = inputString.readlines()

    # remove newlines
    for i in range(0, len(circuitStrings)):
        circuitStrings[i] = circuitStrings[i].rstrip()
    
# parse the input to create the dictionary

createCircuitDict()

doConnection()

# show the circuits
if debug:
    for circuit in circuitDict:
        print(circuit,":",circuitDict[circuit])

if unitTesting:
    testPass = False
    testPassOutput = {"d": {"output" : 72}, "e": {"output" : 507}, "f": {"output" : 492}, "g": {"output" : 114}, "h": {"output" : 65412}, "i": {"output" : 65079}, "x": {"output" : 123}, "y": {"output" : 456}}
    for wire in testPassOutput:
        testPassWire = testPassOutput[wire]["output"]
        circuitWire = circuitDict[wire]["output"]
        if debug:
            print("wire", wire, "test:", testPassWire, "calc:", circuitWire)
        testPass = testPassWire == circuitWire
        if testPass == False:
            break
    print("testPass:", testPass)
else:
    print(circuitDict["a"]["output"])

# this answer for my input is 46065

endTime = time.time() # time in seconds (float)

if timing:
    print("Execution took ", endTime - startTime, " seconds.")

