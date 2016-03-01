import random
weight = 1
class Node:
	p_refs = None #should be None or a list of Node objects (MUST NOT BE A SET)
	_val = None #can be None, 0, or 1. Do not modify this directly, use the getter and setter.
	background = None #should be None or a number between 0 and 1 inclusive
	cpt = None #should be a list of numbers between 0 and 1 with the property that sum(cpt) = 1
	_status = ""
	name = "" #a (hopefully unique) name for each node

	#don't specify that both are none.
	def __init__(self, background = None, p_refs = None, cpt = None, name = ""):

		#a node cannot both have a background probability and parent refs. Parent refs take precedence if both are given.
		if p_refs is not None: #stupid workaround to prevent multiple objects from having the same dict
			self.p_refs = p_refs
			self.cpt = cpt
#			if len(cpt) != 2**len(p_refs):
#				raise ValueError("CPT must have length 2^len(p_refs)")
			self.background = None #to avoid modification of class variable instead of object's variable.
		else:
			if background is None:
				print("Warning: Node created with None for background probability and parent ref dict. Computation will continue, but will probably fail.")
			self.background = background
			self.p_refs = None #to avoid modification of class variable instead of object's variable.
			self.cpt = None
		self._status = "-"
		self.name = name

	#returns 0 or 1. Note: should never return None. 
	#if _val is None when this is called, the node will randomly generate a value based on its parents or, if it has none, its background probability. This is how rejection sampling should work. 
	def getVal(self, reset_val = False):
		output = None
		if self._val is not None:
			output = self._val
		elif self.p_refs is not None and self.cpt is not None:
			binstr = ''
			for p in self.p_refs:
				#binstr.append(str(p.getVal(reset_val = reset_val)))
				binstr = str(p.getVal(reset_val = reset_val)) + binstr
				##print "%s" %binstr
			index = int(binstr, 2) #convert it to binary
			output = (0 if random.random() >= self.cpt[index] else 1)
			#print "index %d node name %s p %f" %(index, self.name, self.cpt[index])
		elif self.background is not None:
			#print "========================="
			#print "node name %s" %self.name
			#print self.background
			output = (0 if random.random() >= self.background else 1)
		else:
			raise TypeError("Improperly initialized Node has no parents and no background probability. getVal function cannot continue")
		
		if reset_val: #the inference procedure cleans up after itself if you say reset_val = True
			self._val = None

		self._val = output
		return output

	#takes None, 0, or 1. Returns nothing.
	def setVal(self, newval):
		if newval in set({None, 0, 1}):
			self._val = newval
		else:
			raise ValueError("setVal function in Node can only take values None, 0, and 1, but was given {0}, a {1}".format(newval, type(newval)))

	def setStatus(self, newstatus):
		if newstatus in {"t", "-", "f", "q"}:
			self._status = newstatus
		else:
			raise ValueError('Set status given argument {0} not in {{"t", "-", "f", "q"}}'.format(newstatus))
	def getStatus(self):
		return self._status

	def updateWeight(self, reset_val = False):
		global weight
		output = None
		if self._val is not None:
			output = self._val
		elif self.p_refs is not None and self.cpt is not None:
			binstr = ''
			for p in self.p_refs:
				#binstr.append(str(p.getVal(reset_val = reset_val)))
				binstr = str(p.getVal(reset_val = reset_val)) + binstr
				##print "%s" %binstr
			index = int(binstr, 2) #convert it to binary
			if self._status == "t":
				output = 1
				weight = weight * self.cpt[index]
			elif self._status == "f":
				output = 0
				weight = weight * (1-self.cpt[index])
			else:
				output = (0 if random.random() >= self.cpt[index] else 1)

		elif self.background is not None:
			if self._status == "t":
				output = 1
				weight = weight * self.background
			elif self._status == "f":
				output = 0
				weight = weight * (1-self.background)
			else:
				output = (0 if random.random() >= self.background else 1)
		else:
			raise TypeError("Improperly initialized Node has no parents and no background probability. getVal function cannot continue")
		
		if reset_val: #the inference procedure cleans up after itself if you say reset_val = True
			self._val = None

		self._val = output
		return output

	def getValue(self):
		return self._val

	def getWeight(self):
		return weight

	def initializeWeight(self):
		global weight
		weight = 1
