"""
Neuronal Net Toolkit - Frontend

@author: Hanno Sternberg <hanno@almostintelligent.de>
@version: 1.0.0


Main class: toolkit

This class provides a control-layer for different Neuronal Nets.
Instead of accessing the nets using a bulky GUI, a small python script does
the work. The advantage of this method is, that everything except for the direct
net control, can be defined by the user. Therefore a basic understandig of
programming and the python language (U{http://docs.python.org/tutorial/index.html}) 
is needed to use this toolkit.

The basic approach towards using this toolkit contains 5 easy steps.

This can be done by writing a script or using the interactive console.

	1. load the toolkit:

		>>> import NNT

	2. create a new toolkit instance:

		>>> toolkit = NNT.Toolkit()

	3. provide the toolkit with information about the netwokr you want to use

		>>> toolkit.init("<type>","<config>")
		
		<type> is the name of the toolkit
		<onfig> is a filename for the configuration file. (can be empty)
		More information on the configuration file structure can be found in the
		net loader documentation

	4. initializing the net
		1. create a new net based on the configuration file
		
			>>> toolkit.create()

		2. load an exisiting net 
		
			>>> toolkit.load("<filename>")

	5. Now it's time to get the net some action (can be done multiple times)

		1. feed the net with data
		
			>>> toolkit.input(<data>)

			<data> must be of the NetLoader.<type>.Config.InputVector Type

		2. train the net 
		
			>>> toolkit.evolve() 
			
			This is only usefull, if new data was fed before (see 5a)

		3. visualize the structure of the net
		
			>>> toolkit.visualize("<filename>")
			
			The resulting file contains the graph in DOT-Language 
			For more information on the DOT-Language please consult http://www.graphviz.org

		4. save the state of the net to a file
		
			>>> toolkit.save("<filename>")
		
	6. At the end you should cleanup your memory
		
			>>> toolkit.cleanup()


"""
__package__ = "NNT"

import NetLoader		# get all available net
import DataLoader		# get all available data loaders
import Visualizer		# get all available visualisation tools

def normalize(val):
	"""
	Normalizes a value
	
	@type  val: number
	@param val: The number to be normalized
	
	@rtype:		number
	@return:	value between -1 and +1
	"""
	if val > 1:
		return 1
	elif val < -1:
		return -1
	else:
		return val

class Toolkit:
	"""
	Main class of the Neuronal Net Toolkit
	
	"""
	
	loader = None
	"""instance of the netloader object"""
	isTypeSet = False
	"""flag if type is set"""
	isCfgSet = False
	"""flag if config is loaded"""
	Loaded = False
	"""flag if net is loaded"""
	type = ""
	"""net type identifier string"""
	cfg = ""
	"""config filename"""
	
	def isInitialized(self):
		"""
		Test if the toolkit is correctly initialised
		
		@rtype:		boolean
		@return:	bool value
		"""
		if self.isTypeSet and self.isCfgSet:
			return True
		else:
			return False
	
	def isLoaded(self):
		"""
		Test if the the toolkit has properly loaded a net
		
		@rtype:		boolean
		@return:	bool result
		"""
		if (self.Loaded):
			return True
		else:
			return False
			
	def getNets(self):
		"""
		Returns a list of all available netloaders
		
		@rtype:		List
		@return:	List of all available netloaders
		"""
		return NetLoader.listNetworks()
	
	# Init Phase
	def setType(self, type):
		"""
		Sets the type of the net
		
		@type	type:	string
		@param	type:	the type-identifier string
		"""
		if not self.Loaded:
			self.type = type
			self.loader = NetLoader.getNetwork(type)
			self.isTypeSet = True
		
	def setConfig(self, cfg):
		"""
		Sets the config of the net
		
		@type	cfg:	string
		@param	cfg:	the filename of the net config
		"""
		if not self.Loaded:
			self.cfg = cfg
			if (cfg != ""):
				self.isCfgSet = NetLoader.loadConfig(self.type,cfg)
			else:
				self.isCfgSet = True
	
	def init(self, type, cfg = ""):
		"""
		Sets type and config of the net
		
		@type	type:	string
		@param	type:	the type-identifier string
		
		@type	cfg:	string
		@param	cfg:	the filename of the net config
		"""
		self.setType(type)
		self.setConfig(cfg)
	
	#Load Phase
	def create(self):
		"""
		Creates a new net
		"""
		if self.isInitialized():
			self.Loaded = self.loader.create()
		
	
	def load(self, filename):
		"""
		Loads a net from a file
		
		@type	filename:	string
		@param	filename:	the filename of the net
		"""
		if self.isInitialized():
			self.Loaded = self.loader.load(filename)

	#Work Phase	
	def save(self, filename):
		"""
		Saves the net the a file
		
		@type	filename:	string
		@param	filename:	the filename of the net
		"""
		if (self.isLoaded()):
			self.loader.save(filename)
	
	def input(self, data, output = None):
		"""
		Feed the net with input data.
		
		@type	data:	inputVector
		@param	data:	input data
		
		@type	output:	outputVector
		@param	output:	optional output vector for training purpose
		"""
		if (self.isLoaded()):
			if output != None:
				self.loader.input(data, output)
			else:
				self.loader.input(data)
			
	def output(self):
		"""
		Reads the output from the net
		
		@rtype:	mixed
		@return: out
		"""
		if (self.isLoaded()):
			return self.loader.output()

	def evolve(self):
		"""
		Let the net evolve
		"""
		if (self.isLoaded()):
			self.loader.evolve()
	
	#Explore Phase
	def visualize(self, filename, options = {'showHead'}): 
		"""
		Visualizes the net using a specified visualisation tool
		
		@type	filename:	string
		@param	filename:	filename where the graph gets stored
		
		@type	options:	set
		@param	options: 	Set of options for visualisation
			possible options:
				- C{'showHead'}: set this flag,
					if you want to have directed connections
				- C{'showLabel'}: activate to display the connection weights
				- C{'useColor'}: colored HTMl
		"""
		Visualizer.useGraphViz(self, filename, options)
		
	#direct access to loader
	def getNet(self):
		"""
		Provides direct access to the netloader
		
		@rtype:	NetLader
		@return: the active netloader
		"""
		return self.loader
		
	def getNeuronCount(self):
		"""
		Returns the number of neurons in the net
		
		@rtype:		int
		@return:	number of neurons
		"""
		return self.loader.getNeuronCount()
		
	def getNeuron(self, index):
		"""
		Returns a single neuron from the net
		
		@type	index:	int
		@param	index:	ID of the Neuron
		
		@rtype:	Neuron
		@return: Neuron
		"""
		return self.loader.getNeuron(index)
		
	def getInputVector(self, data = None):
		"""
		Returns a new instance of the nets inputVector
		
		@type	data:	list
		@param	data:	default data
		
		@rtype:	inputVector
		@return: an inputVector instance
		"""
		return self.loader.getInputVector(data)
		
	def getOutputVector(self, data = None):
		"""
		Returns a new instance of the nets outputVector
		
		@type	data:	list
		@param	data:	default data
		
		@rtype:	outputVector
		@return: an outputVector instance
		"""
		return self.loader.getOutputVector(data)
		
	def cleanup(self):
		"""
		Runs garbage collection on allocated space, to prevent memory-leaks.
		
		This function should be called once at the end of your scriptfile.
		"""
		self.loader.cleanup()
		self.Loaded = False
		