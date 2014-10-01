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
transmittedPerSeed = [] #the AVERAGE transmitted for each seed; use to find mean
timeUnitsPerSeed = [] 
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

	print("%.2f, %.2f %.2f" %computeAverageTransmission(), " (Confidence, Interval) ")
	#print("The average number of transmissions was: ", computeAverageTransmission())
	#print("The throughput was ", computeThroughput())

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
	global F
	global countTimeUnits
	global correctlyRecievedFrames
	global retransmittedFrames
	global transmittedPerSeed

	r = getCheckBits(int(F/K))
=======
	global timeUnitsPerSeed

	seedTime = 0
	transmittedFrames = 0
	random.seed(seed)
	gotFrame = False

	if (K == 0):
		while (not gotFrame):
			countTimeUnits += ((F/K) + A + r)
			seedTime += (A+A)
			countTimeUnits += (A+A)
			if (countTimeUnits >= R):
				break

			if isFrameGoodKequals0():
				gotFrame = True
				correctlyRecievedFrames += 1
				transmittedFrames += 1
				#print("============= Got a good frame =============")
			else:
				retransmittedFrames += 1
				transmittedFrames += 1
				#print("Bad Frame, Retransmitting.....")

		transmittedPerSeed.append(transmittedFrames/correctlyRecievedFrames)
		timeUnitsPerSeed.append(seedTime)
		return

	while (not gotFrame):
		countTimeUnits += ((F/K) + A + r)
		seedTime += (A+A)
		countTimeUnits += (A+A)
		if (countTimeUnits >= R):
			break

		if isFrameGood():
			gotFrame = True
			correctlyRecievedFrames += 1
			transmittedFrames += 1
			#print("============= Got a good frame =============")
		else:
			retransmittedFrames += 1
			transmittedFrames += 1
			#print("Bad Frame, Retransmitting.....")

	transmittedPerSeed.append(transmittedFrames/correctlyRecievedFrames)
	timeUnitPerSeed.append(seedTime)
	return 



# Check if a randomly generated frame passes test
def isFrameGood():
	global K
	global F
	blocks = K
	blockSize = int(F/K)

	#add r to blocksize
	blocksize = blocksize + getCheckBits(blocksize)
	
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
	global transmittedPerSeed
	global T
	if correctlyRecievedFrames != 0:
		#calculate mean
		mean = 0
		for element in transmittedPerSeed:
			mean = mean + element
		mean = mean/5
		#calculate SD
		summation = 0
		for elements in transmittedPerSeed:
			i = ((element-mean)**2)
			summation = summation + i
				
		stdDev = (summation/(T-1))**0.5
		step = 2.776 * (stdDev/(T**0.5))
		lower = mean - step
		upper = mean + step
	else:
		average = 0	
	return mean, lower, upper

def computeThroughput():
	global F
	global correctlyRecievedFrames
	global countTimeUnits
	global transmittedPerSeed
	global timeUnitPerSeed
	global T

	if correctlyRecievedFrames == 0:
		return 0

	else:	
		#challenge here is calculating throughput for each seed first before any of the 
		#other calculations for throughput can occur
		average = ((F*correctlyRecievedFrames)/countTimeUnits)
		summation = 0
		index = 0
		for element in timeUnitPerSeed:
			i = ((F*transmittedPerSeed[index])/element)

			

		return average, lower, upper

# Returns number of HSBC check bits for supplied block size
def getCheckBits(blockSize):
	position = 1
	rBits = 0
	kBits = 0
	K = blockSize

	while kBits <= K: 	# may just need to be less than
		if isPowOfTwo(position):
			rBits += 1
		else:
			kBits += 1
		position += 1
	return rBits

#returns true if Val is a power of 2
def isPowOfTwo(val):
	powers = (1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576, 2097152, 4194304, 8388608, 16777216, 33554432, 67108864, 134217728, 268435456, 536870912, 1073741824, 2147483648, 4294967296, 8589934592, 17179869184, 34359738368, 68719476736, 137438953472, 274877906944, 549755813888, 1099511627776, 2199023255552, 4398046511104, 8796093022208, 17592186044416, 35184372088832, 70368744177664, 140737488355328, 281474976710656, 562949953421312, 1125899906842624)
	if val in powers:
		return True
	else:
		return False


main()


