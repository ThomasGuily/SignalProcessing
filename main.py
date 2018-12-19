import scipy.io.wavfile as wf
import wave as wv
import numpy as np
import matplotlib.pyplot as plt
from Energy import energy
from Preprocessing import makeframe, normalize
from Pitch import pitch
from RuleBased import rulebased
from Formant import formant
from MFCC import mfcc

#MAIN
def main():
	n = 1
	step=15
	width=30
	Mono,fs = normalize('../../audio/cmu_us_bdl_arctic/wav/arctic_a0001.wav')
	ms = makeframe (Mono,width,step,fs)
    # check Preprocessing.py

	pitch (n)
    # check Pitch.py

	y = formant(fs,Mono)
    # check Formants.py

	y = mfcc (fs,Mono)	
    # check MFCC.py

	nbrf = 15 #nbr de fichier aléatoires sélectionnés pour le rule-based system
	rulebased(nbrf) 
	# check RuleBased.py

main()