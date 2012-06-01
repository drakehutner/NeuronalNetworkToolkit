"""
Visualization tools

@author:  Hanno Sternberg <hanno@almostintelligent.de>
@version: 1.0.0


Base class, simple prints the value

"""

class Visualizer:
	"""
	
	"""
	tk = 0
	
	def __init__(self, toolkit):
		"""
		"""
		self.tk = toolkit
	
	def _processNeuron(self, neuron):
		print neuron
		
	def visualize(self):
		for i in range(0, self.tk.getNeuronCount()):
			self._processNeuron(tk.getNet().getNeuron(i))
