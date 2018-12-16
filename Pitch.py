import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as sig
from scipy.signal import find_peaks
from Energy import energy
import random
from Preprocessing import makeframe, normalize

def pitch(data,fs):
    energyf = np.zeros(len(data))
    f0 = np.zeros(len(data))
    threshold = 7
	for k in range (0,len(data)):
        energyf[k] = energy(data[k])
        c =plt.xcorr(data[k], data[k], maxlags=50)
        x = find_peaks(c[1])
        if energyf[k] < threshold:
            f0[k] = 0
		else :
            f0[k] = (x[0][int(len(x[0])/2)] - x[0][int(len(x[0])/2) - 1])
	
	
    return energyf, f0

             
def sceptrum(Mono_splitting,fs):
    '''f0 =[]
    for i in range (len(voice)) :
        if voice[i] == 1 :
             w, h =sig.freqz(Mono_splitting[i],1, worN=None, whole=False, plot=None)
             
             L = 20*np.log10(np.abs(h))
             
             inverse= np
             f0.append(np.max(inverse))
        else:
             
             f0.append(0)
             
    return f0'''
    F0=0
    
    w, h = sig.freqz(Mono_splitting)
    h=np.fft.ifft(20 * np.log10(abs(h)))# The frequency response, as complex numbers.
    h=20 * np.log10(abs(h))  #spectrum
    f=w*fs/(2*np.pi) 
    
    peaks=find_peaks(h)
    #on est dans un domaine temporel
    peaksvalues=[]
    middleIndex = int((np.size(peaks) - 1)/2)
    if(np.size(peaks) != 1):
        F0=(peaks[0][middleIndex+1]-peaks[0][middleIndex])
    return F0

def cepstrum(n):
    step=15
    width=30
    for j in range(1,n+1):
        x = random.randint(1,539)

        if x <=9:

            a = 'a000'+ str(x)
        if x >=10 and x<=99 :

            a ='a00'+ str(x)
		

        if x >=100 and x<=593 :

            a='a0'+ str(x)
            print (a)
        Mono1,fs1 = normalize('../../audio/cmu_us_bdl_arctic/wav/arctic_' + a +'.wav')
        ms1 = makeframe (Mono1,width,step,fs1)
        
        
       


        '''x = random.randint(1,539)
        if x <=9:
            a = 'b000'+ str(x)

        if x >=10 and x<=99 :
            a ='b00'+ str(x)
		

        if x >=100 and x<=593 :
            a='b0'+ str(x)
        print(a)
        Mono2,fs2 = normalize('../../audio/cmu_us_slt_arctic/wav/arctic_' + a +'.wav')
        ms2 = makeframe (Mono2,width,step,fs2)
        

        
        E=[]
        F0=[]
        threshold = 7
        for i in range (0,len(ms1)):
            Ef=energy(ms1[i])
            E.append(Ef)
            """w=signal.hamming(len(ms1[i]))
            ms1[i]= w*ms1[i]"""
            if Ef > threshold:
                F0.append(sceptrum(ms1[i],fs1))
            else:
                F0.append(0)
            print (Ef)
            print ('boucle')
        print (E,F0)
        #F0=np.asarray(F0)'''
       
    