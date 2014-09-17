#!/usr/bin/python3
import sys

# Supplied Vals
A = 500 #feedback time is assumed at 500 bit time units
K = None # number of blocks, chosen such that F is a muliple of K
F = 4000 # Size of frame in bits. assume 4000 bits
e = None # probability that a bit is an error
R = None # Lenght of simulation in bit time units (derived using A)
T = 5 #
Seeds = list()

#	Functions
def main():
	# Handle Arguments
	handleArgs()
	printVals()
	getFrame()


#handle arguments
def handleArgs():
	global A
	global K
	global F
	global e
	global R
	global T
	global Seeds

	# try to take in arguments, also checks right number of args are provided
	try: 
		A = int(sys.argv[1])
		K = int(sys.argv[2])
		F = int(sys.argv[3])
		e = float(sys.argv[4])
		R = int(sys.argv[5])
		T = int(sys.argv[6])
	except:
		print("Bad arguments, please input numbers for all arguments")
		exit()

	# Checks that right number of seeds are provided
	if len(sys.argv) < (7 + T):
		print("not enough seeds")
		exit()
	if len(sys.argv) > (7 + T):
		print("too many seeds")
		exit()

	# Store Seeds as ints
	for i in range(7,(6+T)):
		try:
			Seeds.append(int(sys.argv[i]))
		except:
			print("Please ensure all seeds or integers")		

# Print Values out
def printVals():
	printString = str(A) + " " + str(K) + " " + str(F) + " " + str(e) + " " + str(R) + " " + str(T)

	#append seeds to printString
	for i in Seeds:
		printString = printString + " " + str(i)

	print(printString)
	#print(A, K, F, e, R, T, Seeds)

def isFrameGood():
	return True

# get the next good frame
def getFrame():
	if isFrameGood():
		# we got the frame
		return 
	else:
		#retrnsmit frame\
		return

def isFrameGodd():
	return True
main()





#asumptions
	# All Seeds are ints
	# All args are ints or doubles