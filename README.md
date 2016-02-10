# NamingGame 

Created by Özge Nilay Yalçın 2014 @METU

This is an example of a simple Naming Game simulation. The naming game is a specific case of language games where a population of agents
tries to form a shared lexicon (Vylder and Tuyls, 2006). 

Agents have knowledge about:
	the objects in their environment, 
	how to send and receive signals, and
	the other agents in the environment.

In the agent.py file the agents are constructed with a lexicon for each agent, and functions for sending and receiving messages.
game.py file has the dialog mechanism, how to select conversation partners and keeps a global lexicon file for logging and plotting purposses.
simulation.py has the parameters for the simulation, number of agents in the population, number of objects etc. 
	and plots the success rate of the dialogs with respect to the number of objects.

An important property of this specific type of language strategy the agents have, that agents do not clear their lexicons entirely 
after unsuccessful communication but update their inventories according to a weighted distribution.
	In simulation.py you can see success_delta and failure_delta parameters, and the min/max limits for the weights.
	
Moreover, every agent pair has equal probability of getting selected, which reflects a fully connected population.

To initiate the simulation, just run simulation.py. The logging is incomplete in this version.

Let me know if anything is unclear or if you have problems.
Cheers,
Nilay

Vylder, B. D. and K. Tuyls (2006). How to reach linguistic consensus:A proof of convergence for the naming game. Journal of Theoretical Biology 242(4), 818–831.

