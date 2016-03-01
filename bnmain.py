import sys
from Node import Node
from bnSample import *

#follows method B as defined in the assignment
def readfile(filename = "network_option_b.txt"):
	nodes = {} #associates names with list indices
	output = []
	with open(filename, mode = "r") as f:
		i = 0
		for line in f:
			name = line[0:line.index(":")]
			nodes[name] = i
			output.append(Node(p_refs = [], cpt = [], name = name))
			i += 1
	with open(filename, mode = "r") as f:
		for line in f:
			firstlbracket = line.index("[")
			firstrbracket = line.index("]")
			secondlbracket = line.index("[", firstrbracket)
			secondrbracket = line.index("]", secondlbracket)

			parentnames = line[firstlbracket+1:firstrbracket].split(" ")
			if parentnames == ['']: #is there a better way to do this?
				parentnames = [] 
			name = line[0:line.index(":")]

			(output[nodes[name]].p_refs).extend(map(lambda X: output[nodes[X]], parentnames))

			cpt = list(map(lambda X: float(X), line[secondlbracket+1:secondrbracket].split(" ")))

			if len(parentnames) == 0:
				output[nodes[name]].background = cpt[0]
				output[nodes[name]].p_refs = None
				output[nodes[name]].cpt = None
			else:
				output[nodes[name]].cpt = cpt


	return output

def readqueryfile(filename):
	with open(filename, mode = "r") as f:
		for line in f:
			return line.split(",")

if __name__ == "__main__":
	x = None #define query variable
	evidence = {} #define evidence
	if len(sys.argv) != 4:
		print("usage: python3 bnmain.py <network_file> <query_file> <num_samples>\nwhere <network_file> and <query_file> should be filenames and <num_samples> should be an integer.\nAll arguments are mandatory.")
		sys.exit(1)

	network = readfile(sys.argv[1])
	querydata = readqueryfile(sys.argv[2])

	if len(network) != len(querydata):
		print ("Warning: network(len {0}) and querydata(len {1}) not same size. Execution will continue but will probably not be what you wanted.".format(len(network), len(querydata)))

	#apply query data
	for i in range(0, len(network)):
		if querydata[i] == "?":  
			querydata[i] = "q"
			x = network[i]
		querydata[i] = querydata[i].strip()
		network[i].setStatus(querydata[i])
		if querydata[i] == "t":
			evidence.update({network[i].name: 1})
		elif querydata[i] == "f":
			evidence.update({network[i].name: 0})

	num_samples = int(sys.argv[3])
	'''
	topology = []
	print 'Topology'
	topology = topological_sort(network)
	print topology[0].name
	for t in topology:
		print t.name
	'''
	if x == None:
		print("There is no query variable.")
		sys.exit(1)
	else:
		rs_result = rejection_Sampling(x, evidence, network, num_samples)
		lw_result = likelihood_Weighting(x, evidence, network, num_samples)
		print "Probability Report----------"
		print "Rejection Sampling:  %f" %rs_result
		print "Likelihood Weighting Sampling: %f" %lw_result





