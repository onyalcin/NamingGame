#Created by Özge Nilay Yalçın 2014 @METU

import numpy as np
import string, logging
import random as rnd

class agent:
	def __init__(self, parameters, objects):
		self.lexicon={}
		self.wordlist=[]
		self.objects= objects
		self.parameters = parameters
		for obj in objects:
			self.lexicon[obj] = {}
		
#returning a word for the given object	
	def choose_word(self, object):
		if self.lexicon[object] != {}:
		#selecting the word that has the max value, this could also have been done using probability 	
			max_list = [k for k,v in self.lexicon[object].items() if v == max(self.lexicon[object].values())] #constructs a list with the max value(s)
			if len(max_list) == 1:
				Cword = max_list[0] #returns the max value as the chosen word
				return Cword
			else:
				Cword=(rnd.choice(max_list))  #returns a random word from the list
				return Cword
		else:	#if there is no word for given object, create a new word
			Cword = ''.join(rnd.choice(string.lowercase) for i in xrange(self.parameters['WORD_LENGTH']))
			self.lexicon[object] = {(Cword): self.parameters['MIN_SCORE']}
			return Cword

#returning an object for a given word
	def choose_object(self,word):
		# holds (object, word_score) tuples for easy comparison
		candidate_objects = []
		for obj in self.objects:
			if self.lexicon[obj].has_key(word):
				candidate_objects.append((obj, self.lexicon[obj][word]))
		if len(candidate_objects)!= 0:
			best_score = 0
			best_object = None
			for obj, score in candidate_objects:
				if score > best_score:
					best_object = obj
					best_score = score
				return best_object
		else:
		#if there is no word,obj pair in the lexicon of the agent, than randomly select one object-it doesnt have a strategy
			return rnd.choice(self.objects)
		

	def update(self, isSuccess, object, word):
		if isSuccess == 'isSuccess':
			if self.lexicon[object].has_key((word)):
				score = self.lexicon[object][word]
				self.lexicon[object][word]= min(score + self.parameters['SUCCESS_DELTA'], self.parameters['MAX_SCORE'])
			else:
				self.lexicon[object] = {word: self.parameters['MIN_SCORE']}
		else:
			if self.lexicon[object].has_key((word)):
				score = self.lexicon[object][word]
				self.lexicon[object][word]= max(score - self.parameters['FAILURE_DELTA'], self.parameters['MIN_SCORE'])
			else:
				self.lexicon[object] = {word: self.parameters['MIN_SCORE']}
		
