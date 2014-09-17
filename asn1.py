#!/usr/bin/python3
import sys

# Supplied Vals
A = 500 #feedback time is assumed at 500 bit time units
K = None # number of blocks, chosen such that F is a muliple of K
F = 4000 # Size of frame in bits. assume 4000 bits
e = None # probability that a bit is an error
R = None # Lenght of simulation in bit time units (derived using A)
T = 5 #


#	Functions
def main():
	# Handle Arguments
	checkArgs()
	handleArgs()
	printVals()

# Check for bad arguments
def checkArgs():
	if len(sys.argv) < 7:
		print("Not enough args")
		exit()

#handle arguments
def handleArgs():
	A = sys.argv[1]
	K = sys.argv[2]
	F = sys.argv[3]
	e = sys.argv[4]
	R = sys.argv[5]
	T = sys.argv[6]

# Print Values out
def printVals():
	print(A, K, F, e, R, T, "Plus Seeds go here!")

main()