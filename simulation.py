#Created by Özge Nilay Yalçın 2014 @METU

from game import *
import logging, pylab

class simulation:
	def __init__(self):
		logger= logging.getLogger('start logging')
		logger.setLevel(logging.DEBUG)
		log= logging.FileHandler(filename='example.log', mode='w')
		format=logging.Formatter('%(message)s')
		log.setFormatter(format)
		log.setLevel(logging.INFO)
		logger.addHandler(log)
		noOfAgents= 2
		noOfobjects= 3
		maxObjects= 10
		maxAgents= 100
		timeSteps = 10
		parameters={'WORD_LENGTH': 3, 'MIN_SCORE': 0.1, 'SUCCESS_DELTA':1.0, 'FAILURE_DELTA': 0.2, 'MAX_SCORE': 10.0, 'noOfobjects': noOfobjects, 'noOfAgents': noOfAgents, 'timeSteps': timeSteps}
		logger.info(   "\nnoOfAgents:%i \nnoOfobjects:%i \ntimeSteps:%i \nwordlength:%i \nMIN_SCORE:%f \nSUCCESS_DELTA:%f \nFAILURE_DELTA:%f \nMAX_SCORE:%f \n"  
                         % (noOfAgents,
                            noOfobjects,
                            parameters['timeSteps'],
                            parameters['WORD_LENGTH'],
                            parameters['MIN_SCORE'],
                            parameters['SUCCESS_DELTA'],
                            parameters['FAILURE_DELTA'],
                            parameters['MAX_SCORE']
                            ))
		#runs dialog until convergence
		# g=game(parameters)
		# a=g.dialogTillConverge(parameters)
		# print a
		
		
		#starts dialog for given timestep
		# b=g.dialogGivenTime(parameters)
		# print b
		
		#An example of plotting noOfobjects vs convergence time
		ct=[]  #time of convergence 
		for o in range(1, maxObjects+1): #noofobjects change
			parameters['noOfobjects']= o
			g = game(parameters)
			convergence_time, SuccessRate= g.dialogTillConverge(parameters)
			ct.append(convergence_time)
			print parameters['noOfobjects']
			print ct
			plot(SuccessRate, label=('%iobjects' % o))
			o= o+1
		# plot(ct)
		# xlim(0, maxObjects)
		xlabel('Number of Rounds')
		ylabel('Success Rate')
		legend(loc=4)
		show()
		
s=simulation()
