import scipy.io.wavfile as wf
import wave as wv
import numpy as np
import matplotlib.pyplot as plt
from Energy import energy
from Preprocessing import makeframe, normalize
from Pitch import pitch, cepstrum

#MAIN
def main():
	step=1
	width=3.2
	'''for x in range (1,1133):
		if x <=9:
			a = 'a000'+ str(x)

		if x >=10 and x<=99 :
			a ='a00'+ str(x)
		

		if x >=100 and x<=593 :
			a='a0'+ str(x)
		

		if x >=594 and x<=602:
			a = 'b000'+ str(x-593)


		if x >=603 and x<=692 :
			a ='b00'+ str(x-593)

		if x >=693 :
			a='b0'+ str(x-593)'''
	a = 'a0001'
	print (a)
	Mono1,fs1 = normalize('../../audio/cmu_us_bdl_arctic/wav/arctic_' + a +'.wav')
	Mono2,fs2 = normalize('../../audio/cmu_us_slt_arctic/wav/arctic_' + a +'.wav')
	ms1 = makeframe (Mono1,width,step,fs1)
	ms2 = makeframe (Mono2,width,step,fs2)
	e1,f01 = pitch (ms1,fs1)
	print (e1)
main()