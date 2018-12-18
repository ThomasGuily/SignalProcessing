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
    threshold = 8
    for k in range (0,len(data)):
        energyf[k] = energy(data[k])
        c =plt.xcorr(data[k], data[k], maxlags=50)
        x = find_peaks(c[1])

        if energyf[k] > threshold:
            f0[k] = (x[0][int(len(x[0])/2)] - x[0][int(len(x[0])/2) - 1])
        #if (np.size(x) != 1):
            #f0[k]= (x[0][int(np.size(x[0])/2)])- (x[0][int(np.size(x[0])/2) - 1])
	
    return energyf, f0

             
def sceptrum(data,fs):
    energyf = np.zeros(len(data))
    f0 = np.zeros(len(data))
    threshold = 8
    for k in range (0,len(data)):
        
        energyf[k] = energy(data[k])

        w, h = sig.freqz(data[k])
        #h=np.fft.ifft(20 * np.log10(abs(h)))# The frequency response, as complex numbers. #spectrum
        #f=w*fs/(2*np.pi) 
    
        #x=find_peaks(h)
        
        #on est dans un domaine temporel
        #peaksvalues=[]
    
        #for i in range (10,len(x)-10,1):
            #peaksvalues.append(h[i]) 

        #f0[k]=np.argmax(peaksvalues)

        return f0

def cepstrum(n):
    step=15
    width=30
    itr = 1
    for j in range(0,n):
        x = random.randint(1,539)


        if x <=9:

            a = 'a000'+ str(x)

        if x >=10 and x<=99 :

            a ='a00'+ str(x)
		

        if x >=100 and x<=539 :

            a='a0'+ str(x)
        print (a)


        Mono1,fs1 = normalize('../../audio/cmu_us_bdl_arctic/wav/arctic_' + a +'.wav')
        ms1 = makeframe (Mono1,width,step,fs1)
        ef1,f01 = pitch (ms1,fs1)
        F01 = sceptrum(ms1,fs1)
        
        plt.figure(itr)
        f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex='col', sharey='row')
        f.suptitle('FICHIER artic_' + a +'.wav')

        plt.subplot(221)
        plt.plot(np.linspace(0,(1/fs1)*len(Mono1),num=len(Mono1)),Mono1)
        plt.title('Temporal visualisation : FICHIER artic_' + a +'.wav' )
        plt.xlabel('Time (s)')
        plt.ylabel('Value of the sample')
        plt.subplot(222)
        plt.plot(np.linspace(0,len(ms1),num = len(ms1)),ef1)
        plt.title('Energy frame visualisation' )
        plt.xlabel('Frame number')
        plt.ylabel('Energy of the frame')
        plt.subplot(223)
        plt.plot(np.linspace(0,len(ms1),num = len(ms1)),f01)
        plt.title('Correlation pitch method' )
        plt.xlabel('Frame number')
        plt.ylabel('f0')
        plt.subplot(224)
        plt.plot(np.linspace(0,len(ms1),num = len(ms1)),F01)
        plt.title('Cepstrum pitch method')
        plt.xlabel('Frame number')
        plt.ylabel('F0')
        
        itr = itr +1
        
        
        
        x = random.randint(1,539)

        if x <=9:
            a = 'b000'+ str(x)

        if x >=10 and x<=99 :
            a ='b00'+ str(x)
		

        if x >=100 and x<=539 :
            a='b0'+ str(x)
        print(a)

        Mono2,fs2 = normalize('../../audio/cmu_us_slt_arctic/wav/arctic_' + a +'.wav')
        ms2 = makeframe (Mono2,width,step,fs2)
        ef2,f02 = pitch (ms2,fs2)
        F02 = sceptrum(ms2,fs2)
        print (f02,F02)

        plt.figure(itr)
        f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex='col', sharey='row')
        f.suptitle('FICHIER artic_' + a +'.wav')
        
        plt.subplot(221)
        plt.plot(np.linspace(0,(1/fs2)*len(Mono2),num=len(Mono2)),Mono2)
        plt.title('Temporal visualisation '  )
        plt.xlabel('Time (s)')
        plt.ylabel('Value of the sample')
        plt.subplot(222)
        plt.plot(np.linspace(0,len(ms2),num = len(ms2)),ef2)
        plt.title('Energy frame visualisation' )
        plt.xlabel('Frame number')
        plt.ylabel('Energy of the frame')
        plt.subplot(223)
        plt.plot(np.linspace(0,len(ms2),num = len(ms2)),f02)
        plt.title('Correlation pitch method' )
        plt.xlabel('Frame number')
        plt.ylabel('f0')
        plt.subplot(224)
        plt.plot(np.linspace(0,len(ms2),num = len(ms2)),F02)
        plt.title('Cepstrum pitch method')
        plt.xlabel('Frame number')
        plt.ylabel('F0')

        itr = itr +1

    plt.show()