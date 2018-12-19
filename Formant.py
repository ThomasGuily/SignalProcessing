# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 16:17:03 2018

@author: djakd
"""
from scikit_talkbox_lpc import lpc_ref as lpc
import scipy.io.wavfile as wf
import numpy as np
from Preprocessing import makeframe, normalize
from scipy import signal
import matplotlib.pyplot as plt

def highpass_filter(data,fs):
    order =1 #ordre du filtre
    nyq = 0.5*fs# frequence de nyquist
    cutoff= fs*0.1 #fréquence de coupure
    normal_cutoff = cutoff/nyq # frequence de coupure  normalisé
    b, a = signal.butter(order, normal_cutoff,btype='high')
    y= signal.filtfilt(b, a, data) # on applique le filtre au signale
    return y

def hpfilter2(fs,x,a): 


    xfiltered=signal.lfilter([1., a], [1.], x)

    return xfiltered

def preEmphasis(x,a):#preamphasising

    # application de la formule Formants, point 2.

    temp=np.zeros(len(x))

    

    i=1

    while i <= len(x)-2:

        temp[i-1]=x[i]-a*x[i-1]

        i=i+1

    return temp

def formant(fs,x):
    #calcule des formants
   
    FL= makeframe(x,30,15,fs)
    

    #a=0.63 for pre emphasis

    #shape FL ( 215 x 480)

    i=0

    a=0.67

    while i < len(FL):

        FL[i]=preEmphasis(FL[i],a) # on filtre 

        w=signal.hamming(len(FL[i]))

        FL[i]= w*FL[i]

        FL[i]=lpc(FL[i],int(2+fs/1000))

    
        rts=np.roots(FL[i]) #roots of the lpc's => the formants

        rts = [r for r in rts if np.imag(r) >= 0]

        angz = np.arctan2(np.imag(rts), np.real(rts))

        frqs = sorted(angz * (fs / (2 * np.pi)))

        FL[i]=frqs[1:4] # on recupère les  3 premières valeur

        i=i+1

    FL=FL[:-1]

    return FL


