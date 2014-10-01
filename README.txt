Code By Eden Mar, and Chase McCarty

Assumptions:

	All Seeds are ints
	All args are ints or doubles
	incorrect number of args should cause program to terminate with error message
	R applies to TOTAL time of all trials, not time per frame.
	1 frame is sent per trial 
	Sending AND receiving a frame takes 2A. A to send and A to recieve, 
		retransmits take the same time as initial transmits



what needs fixing:

	[+] R may apply to each trial (for a total of 5) sending as many frames as possible
	[+] Incrementing of Time units may need changing
	[ ] Througput confidence interval function needs to be finished. 


	Report:
		graph with values of K from 0 to 5, and different values of e

		as blocksize increases, average transmissions should increase
		as error increases, average transmissions should increase
		as transmission attempts increase, throughput decreases