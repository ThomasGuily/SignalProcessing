import scipy.io.wavfile as wf
import wave as wv
from scipy.signal import find_peaks
import numpy as np
import matplotlib.pyplot as plt

def normalize(flname):
	fs,data = wf.read(flname,'r')
	print ('fs' + str(fs))
	data = np.array(data)
	maxdata = max(abs(data))
	data = data/maxdata
	print ('data' + str(data))
	#x = batch.getnchannels()
	#print (x)
	#n = batch.getsampwidth()
	#fs = batch.getframerate()
	#print (n,fs)
	#return fs
	return data,fs


def splitting(Mono,width,step,fs):
    # convertion en ms
    step /= 1000 # convertion de ms en s
    width/= 1000
    
    step *= fs #on échantillonne le pas et la fenêtre
    width*= fs
    
    step = int(step)
    width  = int(width) # on le met en entier car correspond aux positions dans la matrice
    
    Mono_splitting = [] # tableau d'echantillon
    
    #normalisation du signal d'entré
    #Mono_norm = normalize(Mono)
    
    #construction du tableau d'echantillon
    i = 0
    while i <= (len(Mono)-width)/step: # i est le nombre d'échantillons
            Mono_splitting.append(Mono[i:(width+i)])#i permet de ce déplacer avec le pas et width+i permet de déplacer la fenêtre   
            i += step
    return Mono_splitting


def energy(data):
	energy=0
	for i in data:
		energy += i**2
	return energy


def energyframe(data):
	
	energyf = np.zeros(len(data))
	f0 = np.zeros(len(data))
	threshold =0
	for i in range (0, len (data)):
		energyf[i]=0
		for j in range (0, len(data[0])):
			energyf[i] += data[i][j]**2
		threshold += energyf[i]

	threshold = threshold/(len (data))

	for k in range (0,len(data)):
		c =plt.xcorr(data[k], data[k], maxlags=50)
		x = find_peaks(c[1])
		if energyf[k] < threshold:
			f0[k] = 0
		else :
			f0[k] = x[0][int(len(x[0])/2)] - x[0][int(len(x[0])/2) - 1]
	
	
	return energyf, threshold , f0



	


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
	ms1 = splitting (Mono1,width,step,fs1)
	ms2 = splitting (Mono2,width,step,fs2)
	#print ('frame1' + str (ms1))
	#print ('frame2' + str (ms2))
	#print (ms)
	#fr = frame(fs,dt,step,size)
	e1 = energy(Mono1)
	e2 = energy(Mono2)
	print (len (Mono1))
	
	
	print ('energy de la personne 1 =' + str (e1))
	print('energy de la personne 2 =' + str (e2))

	ef1, moy1,f01 = energyframe(ms1)
	print ('energy frame1' + str (ef1))
	
	print(f01)
	
	ef2, moy2, f02 = energyframe(ms2)
	print ('energy frame2' + str (ef2))
	
	print(f02)
	#print (energy)

main()