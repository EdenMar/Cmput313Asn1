#! /usr/bin/python3
import sys
import random

# Supplied Vals
A = 500 #feedback time is assumed at 500 bit time units
K = None # number of blocks, chosen such that F is a muliple of K
F = 4000 # Size of frame in bits. assume 4000 bits
e = None # probability that a bit is an error
R = None # Lenght of simulation in bit time units (derived using A)
T = 5 # The number of frames being transmitted. each with it's own seed
Seeds = list()

countTimeUnits = 0
retransmittedFrames = 0
correctlyRecievedFrames = 0

#	Functions
def main():
	# Handle Arguments
	handleArgs()
	printVals()

	# run code T times with different seeds
	for i in range(T):
		getFrame(Seeds[i])
		if countTimeUnits >= R:
			print("Time Limit Reached")
			break

	print("The average number of transmissions was: ", computeAverageTransmission())
	print("The throughput was ", computeThroughput())

	return

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
		print("[X] Bad arguments: Please input numbers for all arguments")
		exit()

	# Checks that right number of seeds are provided
	if len(sys.argv) < (7 + T):
		print("[X] Bad Arguments: Not enough seeds")
		exit()
	if len(sys.argv) > (7 + T):
		print("[X] Bad Arguments: Too many seeds")
		exit()

	# Store Seeds as ints
	for i in range(7,(7+T)):
		try:
			Seeds.append(int(sys.argv[i]))
		except:
			print("[X] Bad Arguments: Please ensure all seeds or integers")

	# Check if K evenly divides F
	if K != 0:
		if F%K != 0:
			print("[X] Bad Arguments: Please ensure that K evenly divides F")
			exit()		

# Print Values out
def printVals():
	printString = str(A) + " " + str(K) + " " + str(F) + " " + str(e) + " " + str(R) + " " + str(T)

	#append seeds to printString
	for i in Seeds:
		printString = printString + " " + str(i)

	print(printString)
	#print(A, K, F, e, R, T, Seeds)

# get the next good frame
def getFrame(seed):
	global A
	global R
	global K
	global countTimeUnits
	global correctlyRecievedFrames
	global retransmittedFrames

	random.seed(seed)
	gotFrame = False

	if (K == 0):
		while (not gotFrame):
			countTimeUnits += (A+A)
			if (countTimeUnits >= R):
				break

			if isFrameGoodKequals0():
				gotFrame = True
				correctlyRecievedFrames += 1
				print("============= Got a good frame =============")
			else:
				retransmittedFrames += 1
				print("Bad Frame, Retransmitting.....")
		return

	while (not gotFrame):
		countTimeUnits += (A+A)
		if (countTimeUnits >= R):
			break

		if isFrameGood():
			gotFrame = True
			correctlyRecievedFrames += 1
			print("============= Got a good frame =============")
		else:
			retransmittedFrames += 1
			print("Bad Frame, Retransmitting.....")
	return 



# Check if a randomly generated frame passes test
def isFrameGood():
	global K
	global F
	blocks = K
	blockSize = int(F/K) # 						# we need to add r here!
	
	#for each block
	for i in range(blocks):
		badBits = 0
		#for each bit
		for j in range(blockSize):
			if badBit():
				badBits += 1
		if badBits > 1:
			return False

	return True

def isFrameGoodKequals0():
	global K
	global F
	blocks = 1
	blockSize = int(F) 
	
	#for each block
	for i in range(blocks):
		badBits = 0
		#for each bit
		for j in range(blockSize):
			if badBit():
				badBits += 1
		if badBits > 0:
			return False
	return True

# determines if a bit is bad or not
# returns true if bit is bad
def badBit():
	global e
	randomInt = random.random()
	if randomInt <= e:
		return True # bit is bad
	else:
		return False

# compute the average number of transmisisons per good frame
def computeAverageTransmission():
	global correctlyRecievedFrames
	global retransmittedFrames
	if correctlyRecievedFrames != 0:
		average = ((correctlyRecievedFrames + retransmittedFrames) / correctlyRecievedFrames)
	else:
		average = 0	
	return average

def computeThroughput():
	global F
	global correctlyRecievedFrames
	global countTimeUnits

	if correctlyRecievedFrames == 0:
		return 0

	return ((F * correctlyRecievedFrames) / countTimeUnits)

main()


