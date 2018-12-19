from Pitch import pitch ,cepstrumpitch
import random
from Preprocessing import makeframe, normalize
import numpy as np

def rulebased(nbr) :
	n=15 #can be changed at any times
	verify = []
	test =[]
	writest = []
	counter = 0
	#different initialisation

	F0mean = pitch(n)
	# n files for each type (bdl/stl) will be analysed, check Pitch.py
	print ('la moyenne des F0 est : '+ str(F0mean))
	#F0mean = initial treshold to compare files value

	for i in range (0,nbr):
		F0meantest, boo = rulebasedtest()
		verify.append(boo)
		#verify contains the real bool values to check if our system works

		'''if boo == 0:
			verify.append('slt')
		if boo == 1:
			verify.append('bdl')'''

		if F0meantest < F0mean : 
			boo2 = 1
			#algorithm thinks it is a 'bdl' file
			test.append(boo2)

		if F0meantest > F0mean : 
			boo2 = 0
			#algorithm thinks it is a 'stl' file
			test.append(boo2)

	if test == verify :
		print ('swaggg 100%')
		#case if we have 100 % of recognition
		print ('real values are : ' + str(verify))
		#print real values (1 =bdl,0=stl)
		print ('rule based test found : ' + str(test))

	else :
		for j in range (0,len(verify)):
			if verify[j] == test [j]:
				counter = counter + 1
			#counter is here to calculate the percentage of recognition

		print ('real values are : ' + str(verify))
		#print real values (1 =bdl,0=stl)
		print ('rule based test found : ' + str(test))
		print ('1 = bdl ; 0 = stl')
		print ('le taux de reconaissance est de '+ str((counter /len(verify))*100) + ' %')



def rulebasedtest() :
	step=15
	width=30
	#same step and same width so we have the same frames

	boo = random.randint (0,1)
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
    
	if boo == 1 :  
		Mono,fs = normalize('../../audio/cmu_us_bdl_arctic/wav/arctic_' + a +'.wav')

	if boo == 0 :  
		Mono,fs = normalize('../../audio/cmu_us_slt_arctic/wav/arctic_' + a +'.wav')
	# a file is selected randomly

	ms = makeframe (Mono,width,step,fs)
	F0 = cepstrumpitch(ms,fs)
	#F0 is calculated for this random file

	F0mean = np.mean(F0)
	#the mean is calculated and returned

	return F0mean,boo #boo is returned to verify ou RuleBasedSystem