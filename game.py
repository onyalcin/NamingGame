# Created by Özge Nilay Yalçın 2014 @METU

import random as rnd
import logging
import numpy as np
from agent import *
from pylab import *

#two loops for the game : dialog lasts until the population converges or dialog lasts until given time frame

class game:
	def __init__(self, parameters):
		## intialize
		self.objects=[]
		self.rounds=[]
		self.words=[]
		self.agents = []
		self.parameters=parameters
		
		for i in range(parameters['noOfobjects']):
			self.objects.append(i)
		
		for index in range(parameters['noOfAgents']):
			self.agents.append((agent(parameters, self.objects), index))		

		
	## dialog
	def dialogTillConverge(self, parameters):
		self.parameters= parameters
		totalSuccess = 0
		successRate= 0
		epsilon=0.05
		t = 1
		while (1-successRate)>epsilon:
			conversationers = rnd.sample(self.agents,2)
			speaker = conversationers[0][0]
			hearer = conversationers[1][0]
			object = rnd.choice(self.objects)
			Cword = speaker.choose_word(object)
			Cobject = hearer.choose_object(Cword)
			if Cobject == object:
				feedback =('isSuccess', object)
				totalSuccess +=1
				print feedback, 'on round:', t
			else:
				feedback=('isFailure', object)
				print feedback, 'on round:' , t
			speaker.update(feedback[0], feedback[1],Cword)
			hearer.update(feedback[0], feedback[1], Cword)
			successRate=(totalSuccess/float(t))
			t+=1
			print successRate
		return t-1

	def dialogGivenTime(self, parameters):
			totalSuccess = 0
			successRate=[]
			timeSteps= parameters['timeSteps']
			for i in range(timeSteps): 
				conversationers = rnd.sample(self.agents,2)
				speaker = conversationers[0][0]
				hearer = conversationers[1][0]
				object = rnd.choice(self.objects)
				Cword = speaker.choose_word(object)
				Cobject = hearer.choose_object(Cword)
				if Cobject == object:
					feedback =('isSuccess', object)
					totalSuccess +=1
					print feedback, 'on round:', i
				else:
					feedback=('isFailure', object)
					print feedback, 'on round:', i
				speaker.update(feedback[0], feedback[1],Cword)
				hearer.update(feedback[0], feedback[1], Cword)
				successRate.append(totalSuccess/float(i+1))
				i+=1
				print i
			return successRate
