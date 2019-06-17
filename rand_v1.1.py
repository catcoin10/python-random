# PRNG version 1.1
from mpmath import sqrt, log
import sys

def middle(text, seed): # find the middle
        length = len(text)
        start = (length / 2) - int(log(seed)) # where to start
        templist = "" # not really a list, but a string list
        retlist = ""
        for i in range(start+3, length): # iterate through items
                templist += text[i] # add to temporary list
        for i in range(len(str(seed))): # populate retlist
                retlist += templist[i]
        return int(retlist)

def prng(seed): # PRNG function, seed must be >= 20 for good results
        cube = seed ** 2 # random number to 4th power
        text = str(cube) # text turned into string
        return middle(text, seed) # find the middle of the string and send it back

seed = int(sys.argv[1])
text = prng(seed) # initialize text variable
for i in range(1, int(input())):
        text = prng(text)
        text2 = prng(text*2)
        deficit = len(str(seed)) - len(str(text)) # how much text we need to add back into the equation
        if deficit > 0: # if we have debt to the text
                text = str(text) # we're going to turn this back to an int when we're done
                text2 = str(text2)
                text += text2[0:deficit]
                text = int(text) # going back
        print(text)
