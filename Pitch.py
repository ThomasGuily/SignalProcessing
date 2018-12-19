import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as sig
from scipy.signal import find_peaks
from Energy import energy
import random
from Preprocessing import makeframe, normalize

def corrpitch(data,fs):

    energyf = np.zeros(len(data))
    f0 = np.zeros(len(data))
    #f0 and energyf initialisation, caution energyf is already a vector of zeros, so there is no need to put a else after the if

    threshold = 8
    #treshold where found by using pitch function with the visualisation

    for k in range (0,len(data)):
        energyf[k] = energy(data[k])
        #check Energy.py to see how we calculate the energy (here for one frame)

        c =plt.xcorr(data[k], data[k], maxlags=50)
        #xcorr have to give the autocorrelation of a specific frame
        x = find_peaks(c[1])

        if energyf[k] > threshold:
            f0[k] = (x[0][int(len(x[0])/2)]- x[0][int(len(x[0])/2) - 1])*16
        #difference between the two picks

    # this function is not working as it should, still, F0 values exist when the energy of the frame is over the treshold
    # but their values seem bad
	
    return energyf, f0

             
def cepstrumpitch(data,fs):
    energyf = np.zeros(len(data))
    f0 = np.zeros(len(data))
    threshold = 8
    
    for k in range (0,len(data)):

        energyf[k] = energy(data[k])
        #check Energy.py to see how we calculate the energy (here for one frame)

        w=sig.hamming(len(data[k]))
        data[k]= w *data [k]
        #hammer window applicated

        w, h = sig.freqz(data[k])
        h=np.fft.ifft(20 * np.log10(abs(h)))
        # The frequency response, as complex numbers. #spectrum
         
    
        x=find_peaks(h)
        # domaine temporel

        if energyf[k] > threshold:
            f0[k] = 2*np.pi/(w[x[0][int(len(x[0])/2)]] - w[x[0][int(len(x[0])/2) - 1]])

            #two values of peaks are sended back to collect corresponding w values 
            # w = 2pi * f , the answer is correctly between 80 and 500 Hz
        
    return f0

def pitch(n):

    #this function is very usefull:
    #putt the value of the input n to 1 if you want to vizualize for 1 bdl file and 1 stl file
    #you can visualize the file values in function of the time, the energy of the frames, and the two pitch methods
    #this function returns a mean for the slt and bdl that is used in de Rule Based System (treshold for de rbs)

    step=15
    width=30
    itr = 1
    
    F0mean1=0
    F0mean2=0
    for j in range(1,n+1):

        x = random.randint (1,1132)
        if x <=9:
            a = 'a000'+ str(x)

        if x >=10 and x<=99 :
            a ='a00'+ str(x)
        
        if x >=100 and x<=593 :
            a='a0'+ str(x)

        if x >=594 and x <=602:
            a = 'b000'+ str(x-593)

        if x >=603 and x<=691 :
            a ='b00'+ str(x - 593)

        if x >=692 :
            a='b0'+ str(x -593)
        print (a)
        # randomfiles are choosen to calculate a mean of F0

        Mono1,fs1 = normalize('../../audio/cmu_us_bdl_arctic/wav/arctic_' + a +'.wav')
        ms1 = makeframe (Mono1,width,step,fs1)
        # check Preprocessing.py

        ef1,f01 = corrpitch (ms1,fs1)
        F01 = cepstrumpitch(ms1,fs1)
        # two methods for pitch estimation, those are located in this file just above this function
        F0mean1 += np.mean(F01)
        #the mean for bdl is stacked here 

        plt.figure(itr)
        f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex='col', sharey='row')
        f.suptitle('FICHIER bdl artic_' + a +'.wav')

        '''plt.subplot(221)
        plt.plot(np.linspace(0,(1/fs1)*len(Mono1),num=len(Mono1)),Mono1)
        plt.title('Temporal visualisation ' )
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
        plt.ylabel('F0')''' #uncomment here to visualize the temporal visualisation for bdl
        
        itr = itr +1
        #used to create figures
        
    

        Mono2,fs2 = normalize('../../audio/cmu_us_slt_arctic/wav/arctic_' + a +'.wav')
        ms2 = makeframe (Mono2,width,step,fs2)
        # check Preprocessing.py
        ef2,f02 = corrpitch (ms2,fs2)
        F02 = cepstrumpitch(ms2,fs2)
        # two methods for pitch estimation, those are located in this file just above this function
        F0mean2 += np.mean(F02)
        #the mean for bdl is stacked here

        '''plt.figure(itr)
        f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex='col', sharey='row')
        f.suptitle('FICHIER slt artic_' + a +'.wav')
        
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
    plt.show()''' #uncomment here to visualize the temporal visualisation for slt

    F0mean1 = F0mean1/n   
    F0mean2 = F0mean2/n
    #means that where stacked before n times need to be divide in consequence 
    print ('bdl mean = ' +str(F0mean1))
    print ('stl mean = ' +str(F0mean2))
    F0mean = (F0mean1 + F0mean2)/2
    #treshold for rulebasedsystem
    return F0mean
    