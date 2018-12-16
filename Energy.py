import numpy as np

def energy(data):
	nrg=0
	for i in data:
		nrg += i**2
	return nrg