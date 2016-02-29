import sys

#follows method B as defined in the assignment
def readfile(filename = "network_option_b.txt"):
	nodes = {} #associates names with list indices
	output = []
	with open(filename, mode = "r") as f:
		i = 0
		for line in f:
			name = line[0:line.index(":")-1]
			nodes[name] = i
			output.append(Node(p_refs = [], cpt = [], name = name))
			i += 1
	with open(filename, mode = "r") as f:
		for line in f:
			firstlbracket = line.index("[")
			firstrbracket = line.index("]")
			secondlbracket = line.index("[", start = firstrbracket)
			#secondrbracket = line.index("]", start = secondlbracket) not needed I think -- FC Feb 29 10:20am

			parentnames = line[firstlbracket,firstrbracket].split(", ")
			name = line[0:line.index(":")-1]

			(output[nodes[name]].p_refs).extend(map(lambda X: output[nodes[X]], parentnames))

			#cpt = map(lambda X: int(X), line[secondlbracket+1:secondrbracket].split(", ")) not needed I think -- FC Feb 29 10:20am
			cpt = map(lambda X: int(X), line[secondlbracket+1:].split(", "))

			if len(parentnames) == 0:
				output[nodes[name]].background = cpt[1]
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
	if len(sys.argv) != 4:
		print("usage: python3 bnmain.py <network_file> <query_file> <num_samples>\nwhere <network_file> and <query_file> should be filenames and <num_samples> should be an integer.\nAll arguments are mandatory."

	network = readfile(argv[1])
	querydata = readqueryfile(argv[2])

	if len(network) != len(querydata):
		print ("Warning: network(len {0}) and querydata(len {1}) not same size. Execution will continue but will probably not be what you wanted.".format(len(network), len(querydata)))

	#apply query data
	for i in range(0, len(network)):
		network[i].setStatus(querydata[i])

	num_samples = int(argv[3])
