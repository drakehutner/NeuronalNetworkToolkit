"""
Network loader object

@author: Hanno Sternberg <hanno@almostintelligent.de>
@version: 1.0.0


Provides access to the different network loaders
"""

__all__ = ["Demo"]

import Demo
import BPN
import SOM


def listNetworks():
	"""	
	@rtype:	list
	@return: list with all available nets
	"""
	return ['Demo']
	
def getNetwork(type):
	"""
	returns the loader object for network-type
	
	@type	type:	string
	@param	type: 	the net identifier string
	
	@rtype: NetLoader
	@return: loader object
	"""
	if (type == 'Demo'):
		return Demo.Network()
		
def loadConfig(type,cfg):
	"""
	returns the loader object for network-type
	
	@type	type:	string
	@param	type: 	the net identifier string
	
	@type	cfg:	string
	@param	cfg: 	filename of the config file
	
	@rtype: boolean
	"""
	if (type == 'Demo'):
		return Demo.loadConfig(cfg)