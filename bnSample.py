
from Node import Node

#sort the nodes in network in topological order
def topological_sort(network):
	searched = []
	topology = []
	for node in network:
		if node not in searched:
			search(network, node, searched, topology)
	return topology

def search(network, node, searched, topology):
	searched.append(node)
	if (node.p_refs != None):
		for p in node.p_refs:
			if p not in searched:
				search(network, p, searched, topology)
	topology.append(node)

def clearNetwork(network):
	for node in network:
		node.setVal(None)


def rejection_Sampling(x, e, network, num):
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
	for j in range(0, num):
		clearNetwork(network)
		event = prior_sample(network) #generates a rondom event
		if (isConsistant(event, e)): #if the event is consistant with evidence
			n = n + 1	
			if (x.getValue() == 1): #if the value of the query variable is true
				m = m + 1
	#print "n is %d" %n
	#print "m is %d" %m
	return normalize(m, n) #calculate m/n

#check if he event is consistent with the evidence
def isConsistant(x, e): #evidence is a dictionary which is read from the query file
	for i in e:
		if e[i] != x[i]:
			return False
	return True

#calculate the probability
def normalize(m, n):
	if n == 0:
		return 0
	return float(m)/n
#generate a random event
def prior_sample(network):
	topology = []
	event = {}
	topology = topological_sort(network)
	for node in topology:
		val = node.getVal()
		event.update({node.name: val})	
	return event

#generate a event which is consistent with the evidence
def weight_sample(network):
	topology = []
	event = {}
	topology = topological_sort(network)
	for node in topology:
		val = node.updateWeight()
		event.update({node.name: val})	
	return event


def likelihood_Weighting(x, e, network, num): 
	xTrueWeight = 0
	allWeights = 0
	count = 0
	event = {}
	for i in range(0, num):
		clearNetwork(network) #Set the value of node(true, false) to none 
		x.initializeWeight()	#initialize weight to 1		
		event = weight_sample(network) #generates a event that is consistent with give evidence
		weight = x.getWeight() #get the updated weight
		allWeights += weight  #adds weight to total weight
		if(x.getValue() == 1): #if the query variable is true
			xTrueWeight += weight  #is x is true in this event, add one to x True weight
	return normalize(xTrueWeight, allWeights) #normalize the probability
