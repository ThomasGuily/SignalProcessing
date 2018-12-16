import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks
from Energy import energy
import random

def pitch(data,fs):
	
	energyf = np.zeros(len(data))
	f0 = np.zeros(len(data))
	threshold = 6.5
	for i in range (0, len (data)):
		energyf[i] = energy(data[i])
		

	for k in range (0,len(data)):
		c =plt.xcorr(data[k], data[k], maxlags=50)
		x = find_peaks(c[1])
		if energyf[k] < threshold:
			f0[k] = 0
		else :
			f0[k] = (x[0][int(len(x[0])/2)] - x[0][int(len(x[0])/2) - 1])
	
	
	return energyf, f0

    def cepstrum-based_pitch

        for i in range(1,6)
            random.randint(1,593)
            if x <=9:
			    a = 'a000'+ str(x)

		    if x >=10 and x<=99 :
			    a ='a00'+ str(x)
		

		    if x >=100 and x<=593 :
			    a='a0'+ str(x)

            Mono1,fs1 = normalize('../../audio/cmu_us_bdl_arctic/wav/arctic_' + a +'.wav')
		
        for i in range(	1,6)
			random.randint(1,593)
		    if x <=9:
			    a = 'b000'+ str(x)

		    if x >=10 and x<=99 :
			    a ='b00'+ str(x)
		

		    if x >=100 and x<=593 :
			    a='b0'+ str(x)

	        Mono2,fs2 = normalize('../../audio/cmu_us_slt_arctic/wav/arctic_' + a +'.wav')