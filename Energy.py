import numpy as np

def energy(data):
	nrg=0
	for i in data:
		nrg += i**2
	# this function work if data is a vector
	return nrg

