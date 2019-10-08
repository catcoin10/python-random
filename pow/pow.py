# This program uses input() for input.
# To use in a command line fashion, run like this:
# echo NUMBER | python rng.py
# To use in a Python fashion, run the program with no args and then type your number
# Note: the letters q and y are removed from the alphabet. To use their phonetic equivalents, type kw and i, respectively

# import
from mpmath import sqrt, log
from secrets import randbits

# functions
def middle(text, seed): # find the middle
	length = len(text)
	start = (length // 2) - int(log(seed)) # where to start
	templist = "" # not really a list, but a string list
	retlist = ""
	for i in range(start+3, length): # iterate through items
		templist += text[i] # add to temporary list
	for i in range(len(str(seed))+1): # populate retlist
		retlist += templist[i]
	return int(retlist)

# this program does NOT use the MSM per se.
def prng(seed): # PRNG function, seed must be >= 20 for good results
	cube = seed ** 2 # random number to 4th power
	text = str(cube) # text turned into string
	return str(middle(text, seed))[:20] # find the middle of the string and send it back, we will only need 15 digits

def black_iverson(input): # "Black Iverson" turns zeroes into ones and ones into zeroes
        x = bin(int(input))[2:] # gather the binary number
        new_x = ""
        for i in x: # we need to iterate to do the replacement
                new_x += str((int(i) + 1) % 2)
        return new_x[1:] # we take the first char out because the 1st character is always a zero

def pow(digits=2): # proof of work algorithm using random numbers. the number is how many digits
        out = "3"
        while out[:digits] != "9"*digits:
                data = randbits(60) # we only need 64 bits; we're not bitcoin so we can do this without filling the space completely
                out = str(prng(data))
        return data

print(pow(5))
