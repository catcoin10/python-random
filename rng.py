# This program uses input() for input.
# To use in a command line fashion, run like this:
# echo NUMBER | python rng.py
# To use in a Python fashion, run the program with no args and then type your number

from mpmath import sqrt, log

def middle(text, seed): # find the middle
	length = len(text)
	start = (length / 2) - int(log(seed)) # where to start
	templist = "" # not really a list, but a string list
	retlist = ""
	for i in range(start+3, length): # iterate through items
		templist += text[i] # add to temporary list
	for i in range(len(str(seed))+1): # populate retlist
		retlist += templist[i]
	return int(retlist)

# this program does NOT use the MSM per se.
def prng(seed): # PRNG function, seed must be >= 20 for good results
	cube = seed ** 4 # random number to 4th power
	text = str(cube) # text turned into string
	return middle(text, seed) # find the middle of the string and send it back

seed = 172 # we need to use a seed
text = prng(seed) # initialize text variable
for i in range(1, int(input())): # initialize the program
	text = prng(text) # develop the data
print(text)
