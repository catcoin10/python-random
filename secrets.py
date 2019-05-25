import secrets, sys, mpmath
def random_integer(n):	return secrets.randbits(n) + 1 # generate random number between 1 and 2^n

max = int(sys.argv[1]) # numbers between 1 and n
n = random_integer(int(mpmath.log(max,2))+1) # generate random number

while n >= max+1:  n = random_integer(int(mpmath.log(max,2)+1))

fd = open("random.txt", "r")	
i = int(fd.read()) + int(mpmath.log(max,2)+1)
fd.close()
fd = open("random.txt", "w")
fd.write(str(i))

print(n)
