# PRNG version 1.2
# PoW implementation

from mpmath import sqrt, log
import sys
from secrets import randbits

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
        print(cube)
        text = str(cube) # text turned into string
        return middle(text, seed) # find the middle of the string and send it back, we will only possibly ever need 25 digits

def black_iverson(input): # "Black Iverson" turns zeroes into ones and ones into zeroes
        x = bin(int(input))[2:] # gather the binary number
        new_x = ""
        for i in x: # we need to iterate to do the replacement
                new_x += str((int(i) + 1) % 2)
        return new_x[1:] # we take the first char out because the 1st character is always a zero

def pow(digits=2): # proof of work algorithm using random numbers. the number is how many digits
        out = 3
        while black_iverson(out)[:digits] != "0"*digits:
                data = randbits(64) # we only need 64 bits; we're not bitcoin so we can do this without filling the space completely
                print(data)
                out = prng(data)
                print(out)
        return data
