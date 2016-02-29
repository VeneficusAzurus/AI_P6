
def rejection_Sampling(x, e, num):
	"""
	X the query variable
	e evidence specified as an evidence
	bn a Bayesian network
	num the total number of samples to be generated
	local variables: N a vector of counts over X, initially zero
	"""
	n = 0
	m = 0
	event = {}
	for j in range(1, num+1):
		event = x.getVal(true)
		if (isConsistant(event, e)):
			n = n + 1
		if (x._val == 1):
			m = m + 1
	return normalize(m, n)

def isConsistant(x, e):
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
		event = x.weight_Sample(true)
		w = x.getWeight()
		allWeights += w
		if(x._val == 1):
			xTrueWeight += w
	normalize(xTrueWeight, allWeights)




			

		