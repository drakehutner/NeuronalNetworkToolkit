"""
GraphViz Visualizer

@author: Hanno Sternberg <hanno@almostintelligent.de>
@version: 1.0.0


"""

import Colors			# get colors
from visualizer import Visualizer

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

class GraphViz(Visualizer):
	"""
	
	"""
	
	def _processNeuron(self, file, neuron, options = {}):
		"""
		Part of the graphviz visualisation routines
		Adds a single neuron and its connections into the graph
		
		@type	file:	filehandle
		@param	file:	handle of the graph file
		
		@type	neuron:	neuron
		@param	neuron:	the neuron
		
		@type	options:	set
		@param	options: 	Set of options for visualisation
			Further documentation: L{visualize}
		"""
		if (neuron != 0):
			mass = normalize(neuron.getMass())
			if (mass < 0):
				mass_p = round(100+(mass*100))
			else:
				mass_p = round(100-(mass*100))
			if 'useColor' in options:
				color = int(neuron.getName().split('.')[1])
				file.write('\t%s [shape="box" color="grey%i" penwidth="3" style="filled" fillcolor="%s"]\n' % (neuron.getName(),mass_p,Colors.getColor(color)))
			else:
				file.write('\t%s [shape="box" color="grey%i" penwidth="3"]\n' % (neuron.getName(),mass_p))
			for x in range (0, neuron.getLinkCount()):
				weight = normalize(neuron.getWeight(x))
				if (weight < 0):
					weight_p = round(100+(weight*100))
				else:
					weight_p = round(100-(weight*100))
				file.write("\t%s -> %s " % (neuron.getName(),neuron.getLink(x)))
				file.write(' [')
				if 'showLabel' in options:
					file.write('label="%.2f" ' % (weight))
				if 'showHead' not in options:
					file.write('arrowhead="none" ')
				file.write('color="grey%i"] /* weight: %.2f */' % (weight_p,weight))
				file.write('\n')
			file.write('\n')
	
	#Explore Phase
	def visualize(self, filename, options = {'showHead'}): 
		"""
		Visualizes the net using graphviz.
		This function creates a file in dot-language.
		To get a PNG you need GraphViz installed on your machine and
		use the following command: DOT -Tpng -O <graphfile>
		
		@type	filename:	string
		@param	filename:	filename where the graph gets stored
		
		@type	options:	set
		@param	options: 	Set of options for visualisation
			possible options:
				- C{'showHead'}: set this flag,
					if you want to have directed connections
				- C{'showLabel'}: activate to display the connection weights
				- C{'useColor'}: colored Nodes
		"""
		file = open(filename, "w")
		file.write("digraph G {\n")
		file.write("node [shape=box]\n")
		for i in range(0, self.tk.getNeuronCount()):
			self._processNeuron(file, self.tk.getNeuron(i), options)
		file.write("}\n")
		file.close()
	