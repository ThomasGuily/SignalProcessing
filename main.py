import scipy.io.wavfile as wf
import wave as wv
import numpy as np
import matplotlib.pyplot as plt
from Energy import energy
from Preprocessing import makeframe, normalize
from Pitch import pitch, cepstrum


#MAIN
def main():
	
	n = 1
	cepstrum(n)
main()