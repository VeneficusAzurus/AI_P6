
def rejection_Sampling(x, e, num):
	"""
	X the query variable
	e evidence specified as an evidence 
	(is a dictionary whose keys are node name and values are status reading from query file)
	bn a Bayesian network
	num the total number of samples to be generated
	local variables: N a vector of counts over X, initially zero
	"""
	n = 0
	m = 0
	event = {}
	for j in range(1, num+1):
		event = prior_sample() #generates a rondom event
		if (isConsistant(event, e)): #if the event is consistant with evidence
			n = n + 1	
		if (x.getTempVal() == 1):
			m = m + 1
	return normalize(m, n) #calculate m/(m+n)

def isConsistant(x, e): #evidence is a dictionary which is read from the query file
	for i in x:
		if (x[i] != e[i]):
			return false
	return true

def normalize(m, n):
	return m/(m+n)

def likelihood_Weighting(x, e, num): 
	xTrueWeight = 0
	allWeights = 0
	event = {}
	for i in range(1, num+1):
		event = x.weight_sample() #generates a event that is consistent with give evidence
		w = x.getWeight()  #gets updated weight
		allWeights += w  #adds weight to total weight
		if(x.getTempVal() == 1):
			xTrueWeight += w  #is x is true in this event, add one to x True weight
	return normalize(xTrueWeight, allWeights) #normalize the probability




			

		