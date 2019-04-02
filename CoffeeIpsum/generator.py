'''

'''

from mpmath import sqrt, log
import time # allow sleep, no from sleep import time

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

def auxprng(seed): # PRNG function, seed must be >= 20 for good results
	cube = seed ** 4 # random number to 4th power
	text = str(cube) # text turned into string
	return middle(text, seed) # find the middle of the string and send it back

def prng(seed, rounds):
	rounds = rounds * 2
	text = auxprng(seed) # initialize text variable
	for i in range(1, rounds):
		text = auxprng(text)
	text = str(text)
	if (len(text) % 2) == 1:	text += text[0]
	return text

def period(number): # determine if we need a period
	if (number % 10) == 0:	return '. ' # we are feeding 2 birds with 1 scone here
	else:			return ' ' # just a space

def count_space(str): # count the number of spaces in a string
	spaces = 0 # initialize variable
	for i in str:
		if i == " ":	spaces += 1 # increment space count
	return spaces

def trim(str): # make the string smaller
	x = count_space(str) # get the space count
	new_list = str.split(" ")[x-50:x-1]
	new_str = ""
	for i in new_list:	new_str += i + " "
	return new_str # bye

def ipsum(x): # how many
	n = prng(636174, x) # seed is hex of the word cat
	list = map(''.join, zip(*[iter(n)]*2))
	words = ["brew", "aged", "cafe", "espresso", "caffeine", "brown", "robust", "mocha", "filter", "delicious", "italy", "bean", "thin", "cream", "fruit", "sugar", "delight", "morning", "think", "shot"] * 5
	text = ""

	count = 0 # initialize count variable.
	for i in list:
#		print(count)
		x = words[count%100]
		text += x; text += period(int(i))
		count += 1
	return text # send text back

# generate random ipsum lines

x = 57 # a good starting number
while True:
	print(trim(ipsum(x)))
	time.sleep(4)
	x += 50
