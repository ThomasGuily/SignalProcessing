import scipy.io.wavfile as wf
import numpy as np

def normalize(flname):
	fs,data = wf.read(flname,'r')
	data = np.array(data)
	maxdata = max(abs(data))
	data = data/maxdata
	#normalisation
	
	return data,fs

def makeframe(Mono,width,step,fs):
    # convertion en ms
    step = int((step*fs)/1000) # convertion de ms en s
    width= int((width*fs)/ 1000)
    #on échantillonne le pas et la fenêtre
    # on le met en entier car correspond aux positions dans la matrice
    
    Mono_splitting = [] # tableau d'echantillon
    
    #normalisation du signal d'entrée
    #Mono_norm = normalize(Mono)
    
    #construction du tableau d'echantillon
    i = 0
    while i <= (len(Mono)-width): # i est le nombre d'échantillons
            Mono_splitting.append(Mono[i:(width+i)])#i permet de ce déplacer avec le pas et width+i permet de déplacer la fenêtre   
            i += step
    return Mono_splitting