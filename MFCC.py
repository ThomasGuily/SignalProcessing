import scipy.io.wavfile as wf
import numpy as np
from Preprocessing import makeframe, normalize
from scipy import signal
import matplotlib.pyplot as plt
from filterbanks import filter_banks
from scipy.fftpack import dct

def preEmphasis2(x,a=0.97):#filtre

    # application de la formule Formants, point 2.

    temp=np.zeros(len(x))

    

    i=1

    while i <= len(x)-2:

        temp[i-1]=x[i]-a*x[i-1]

        i=i+1

    return temp

def hamming(x,fs):
    split = makeframe(x,30,15,fs)
    i=0
    while i < len(split):
        w = signal.hamming(len(split[i]))
        split[i] = w*split[i]
        i=i+1
    
    return split

def powerspectrum(split):
   # calcul de la puissance du spectre
    i=0
    NTFD = 512
    while i < len(split):
        split[i] = (np.abs(np.fft.fft(split[i]))**2)/(2*NTFD) #formule de la puissance
        i=i+1
    return split
def mfcc(fs,x):
    
    a = 0.97
    
    x= preEmphasis2(x,a)
    
    split = hamming(x,fs)
    
    temp=(len(split[0])*2)-1
    
    powf = powerspectrum(split)
    
    
    filterbv= filter_banks(powf,fs,nfilt = 40,NFFT = temp)
    
    mfccsvector = dct(filterbv,type=2,axis=1,norm='ortho')
    
    MFCC =mfccsvector[:,0:13] #on ne prend que les 13 premiere valeurs
    
    
    return MFCC
