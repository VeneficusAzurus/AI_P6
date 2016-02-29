if __name__ == "__main__":
	def readfile(filename):
		nodes = {}
		with open(filename, mode = "r") as f:
			for line in f:
				name = line[0:line.index(":")-1]
				nodes[name] = Node(p_refs = [], cpt = [], name = name)
		with open(filename, mode = "r") as f:
			for line in f:
				firstlbracket = line.index("[")
				firstrbracket = line.index("]")
				secondlbracket = line.index("[", start = firstrbracket)
				secondrbracket = line.index("]", start = secondlbracket)

				parentnames = line[firstlbracket,firstrbracket].split(" ")
				name = line[0:line.index(":")-1]

				for pname in parentnames:
					nodes[name].p_refs.append(nodes[pname])

				cpt = map(lambda X: int(X), line[secondlbracket+1:secondrbracket].split(" "))

				if len(parentnames) == 0:
					nodes[name].background = cpt[1]
					nodes[name].p_refs = None
					nodes[name].cpt = None
				else:
					nodes[name].cpt = cpt

		return nodes