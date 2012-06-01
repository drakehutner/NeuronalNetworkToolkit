"""

Color list for colored graphs

@author: Hanno Sternberg <hanno@almostintelligent.de>
@version: 1.0.0



"""

__package__ = "visualizer"

def getColor(index):
	"""
	Returns a color to a given index
	
	@type	index:	int
	@param	index:	color index
	
	@rtype:	string
	@return: color
	"""
	colors = [
		'white',
		'red',
		'green',
		'blue',
		'yellow',
		'brown',
		'coral',
		'crimson',
		'cyan',
		'darkgreen',
		'darkorange',
		'firebrick',
		'gold',
		'deeppink',
		'violet',
		'forestgreen',
		'greenyellow',
		'grey',
		'hotpink',
		'indigo',
		'limegreen',
		'navy',
		'saddlebrown',
		'deepskyblue',
		'purple'
	]
	return colors[index % len(colors)]