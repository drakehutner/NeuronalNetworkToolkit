"""
network loader for the demo network
The demo network is a BPG-network without learning possibility
It's input vector has 5 elements, the output has 2 elements

@author: Hanno Sternberg <hanno@almostintelligent.de>
@version: 1.0.0


"""
from ctypes import *

# Static configuration class
# Holds all configuration information
class Config:
	"""static demo net configuration class"""
	
	inputLength = 5
	"""Length of input vector"""
	outputLength = 2
	"""Length of the output vector"""
	internalLayerCount = 2
	"""number of internal layers"""
	neuronCount = 17
	"""total number of neurons"""
	links = (0,0,0,0,0,2,2,2,1,1,1,2,2,2,3,3,1)
	"""Connection matrix"""
	layerLength = (6, 4, 2)
	"""List with all layer sizes"""
	DataType = c_float
	"""data type of the neurons"""
	InputVec = c_float * 5
	"""inputVector type"""
	OutputVec = c_float * 2
	"""outputVector type"""
	
def updateConfig():
	"""
	Updates the configuration
	since this net is static, there is nothing to do.
	"""
	pass
		
def loadConfig(filename):
	"""
	loads a new configuration
	since the net is static, there is nothing to do here.
	"""
	return True

# Neuron information class
# 
class Neuron:
	"""Neuron class for demo net"""

	def __init__(self, name, links, weights):
		"""
		@type	name:	int
		@param	name:	Identifier of the neuron
		
		@type	links:	list
		@param	links: 	list with all connections
		
		@type	weights:	list
		@param	weights:	list of the weights to the connectet neurons
		"""
		self.ID = name
		self.links = []
		self.weights = []
		for i in range(0, len(links)):
			self.links.append(str(links[i]))
			self.weights.append(round(weights[i],2))
			
	def getWeight(self, index):
		"""
		Returns the weight of a connection
		
		@type	index:	int
		@param	index:	position in the connection list
		
		@rtype:	float
		@return: weight
		"""
		return self.weights[index]
		
	def getLink(self, index):
		"""
		Returns the ID of a link
		
		@type	index:	int
		@param	index:	position in the link list
		
		@rtype:	int
		@return: link ID
		"""
		return self.links[index]
		
	def getLinkCount(self):
		"""
		Return the number of connections
		
		@rtype: int
		@return: number of connections
		"""
		return len(self.links)
		
	def getName(self):
		"""
		Returns the name of the neuron
		
		@rtype: int
		@return: name of the neuron
		"""
		return self.ID
		
	def getMass(self):
		"""
		Returns the mass of the neuron
		
		The mass is resolved as the neuron bias value.
		
		@rtype:	float
		@return: neuron mass
		"""
		return 1


class Network:
	"""
	Custom Netloader for Demo net
	"""
	hnd = 0
	"""Library handle"""

	def __init__(self):
		"""
		loads the library and initialises the net
		"""
		self.hnd = CDLL("demo.dll")
		self.hnd.init()
		self._update()
		
			
	def _update(self):
		self.InputVector = Config.InputVec
		self.OutputVector = Config.OutputVec
		
	def create(self):
		"""
		creates a new net
		since the demo net is static the function does nothing
		@rtype: Boolean
		"""
		return True
		
	def load(self, filename):
		"""
		loads an existing net
		
		@type	filename:	string
		@param	filename:	filename of the file containing the net
		
		@rtype:	boolean
		"""
		if (self.hnd.loadState(filename) == 0):
			return True
		else:
			return False
	
	def save(self, filename):
		"""
		Saves the net into a file
		
		@type	filename:	string
		@param	filename:	filename of the destination file
		
		@rtype:	boolean
		"""
		if(self.hnd.saveState(filename) == 0):
			return True
		else:
			return False
		
	def input(self, data):
		"""
		feeds the net with new data
		
		@type	data: inputVector
		@param	data: the input data
		"""
		self.hnd.inputData(data)
		self.hnd.process()
		
	def output(self):
		"""
		reads the output value of the net
		
		@rtype: outputVector
		@return: outputVector
		"""
		out = Config.OutputVec()
		self.hnd.getVector(out)
		return out
	
	def getNeuron(self, index):
		"""
		Returns a neuron object
		
		@type	index:	int
		@param	index:	ID of the Neuron
		
		@rtype:	Neuron
		@return: Neuron object
		"""
		linkcnt = Config.links[index]
		WeightVec = Config.DataType * linkcnt
		NeuronName = c_char_p
		NeuronNameVec = NeuronName * linkcnt
		NeuronNameRef = NeuronName * 1
		weights = WeightVec()
		links = NeuronNameVec()
		name = NeuronNameRef()
		self.hnd.getNeuron(index, name, links, weights, c_int(linkcnt))
		return Neuron(name[0], links, weights)
		
	def getNeuronCount(self):
		"""
		Calculates the number of neurons
		
		@rtype:	int
		@return: number of neurons
		"""
		return Config.neuronCount;
	
	def evolve(self):
		"""
		let the net evolve
		
		"""
		pass
	
	def cleanup(self):
		"""
		garbage collection
		"""
		self.hnd.cleanup()
		
	def _getVector(self, vec, data):
		"""
		Fills a vector with data
		
		@type	vec:	vector
		@param	vec:	target vector
		
		@type	data:	list
		@param	data:	data for the vector
		
		@rtype:	vectorType
		"""
		for i in range(0, len(vec)):
			vec[i] = data[i]
		return vec		
		
	def getInputVector(self, data = None):
		"""
		
		@type	data:	list
		@param	data:	data for the vector
		
		@rtype:	InputVector
		"""
		if (data != None):
			return self._getVector(Config.InputVec(),data)
		else:
			return Config.InputVec()
		
	def getOutputVector(self, data = None):
		"""
		
		@type	data:	list
		@param	data:	data for the vector
		
		@rtype:	InputVector
		"""
		if (data != None):
			return self._getVector(Config.OutputVec(),data)
		else:
			return Config.OutputVec()	

		