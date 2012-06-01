"""
Neuronal Network Toolkit - Testing Tool

@author: Hanno Sternberg <hanno@almostintelligent.de>
@version: 1.0.0

Training And Testing The Net

The three steps to success

	1. initialize the tool
		Therefor an initialized instance of the NNT is needed

		>>> test = TestTool(<toolkit>)

	2. load your data

		>>> test.loadData(<datafile>)

	3. run the training

		>>> test.train(<number of runs>, <number of visualisation steps>)

optionally you can specify additional options for the visualization

	>>> test.setVisOptions(<filemask>, <set of options>)
	
<filemask> specifies the mask which is applied to the filename. Default value: "TrainingRun_%.4i.gv"

<set of options>: {'showLabel', 'showHead', 'useColor'}
	
"""

import DataLoader

class TestTool:
	"""
	Simple net training class
	"""
	
	def __init__(self, toolkit):
		"""
		constructor
		
		@type	toolkit: Toolkit
		@param 	toolkit: reference to a fully initialized toolkit
		"""
		self.tk = toolkit
		self.visMask = "TrainingRun_%.4i.gv"
		self.visOptions = {}
		self.data = None
	
	def loadData(self, datafile):
		"""
		Load a datafile
		
		@type 	datafile:	string
		@param	datafile:	Filename of the datafile
		"""
		self.data = DataLoader.SimpleTextReader(datafile)

	def setVisOptions(self, fileMask, options = {}):
		"""
		
		@type	fileMask:	string
		@param	fileMask:	Mask, which is applied to the filename
			needs a integer variable for training-run number
			
		@type	options:	set
		@param	options:	set of options
		"""
		self.visMask = fileMask
		self.visOptions = options
	
	def train(self, runs, save):
		"""
		start a training run
		
		@type	runs:	int
		@param	runs:	number of training runs 
		
		@type 	save:	int
		@param	save:	number of steps, between two visualisations
		"""
		for run in range(0,runs+1):
			if (run % save == 0):
				print "Run %i of %i" % (run, runs)
			while not self.data.eof():
				inpVec = self.data.convertInput2Vec(self.tk.getInputVector())
				outVec = self.data.convertOutput2Vec(self.tk.getOutputVector())
				#send data to network
				self.tk.input(inpVec, outVec)
				#train the network
				self.tk.evolve()
				self.data.next()
				if (run % save == 0):
					#visualize network after learning 
					self.tk.visualize(self.visMask%(run),self.visOptions)
			self.data.reset()
