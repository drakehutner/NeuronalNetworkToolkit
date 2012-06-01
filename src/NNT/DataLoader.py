"""
Data Loader

@author: Hanno Sternberg <hanno@almostintelligent.de>
@version: 1.0.0



"""
from ctypes import *


class SimpleTextReader:
	"""
	This class can read data files in the following format.

	Each line contains a pair of input and output vectors.
	The two vectors are separeted by a colon (":").
	Each vector is a space separeted list of floating point values.
	
	BNF::
		file          ::= <line>
		<line>        ::= <inputVector>:[<outputVector>][:<label>]\\n[<line>]
		<inputVector> ::= <value>[ <inputVector>]
		<outputVector>::= [<value>[ <outputVector>]]
		<value>       ::= floating point number
		<label>       ::= String
	
	"""
	def __init__(self, filename):
		"""
		
		@type	filename:	string
		@param	filename:	the datafile
		"""
		self.reset() 
		self.data = []
		
		fHnd = open(filename, 'r')
		lines = fHnd.readlines()
		fHnd.close()
		
		for line in lines:
			self._parseLine(line)

	def _parseNumber(self, str):
		"""
		parses a number into a int or float type
		
		@type	str:	string
		@param	str:	input string
		
		@rtype:	int | float
		@return:	number
		"""
		if (str.count(".") == 0):
			return int(str)
		if (str.count(".") == 1):
			return float(str)
		return str
		
	def _parseVec(self, str):
		"""
		parses a vector into a list
		
		@type	str:	string
		@param	str:	input string
		
		@rtype:	list
		@return: vector
		"""
		vec = []
		splt = str.split()
		for i in range(0,len(splt)):
			vec.append(self._parseNumber(splt[i]))
		return vec
	
	def _parseLine(self, line, delimiter = ":"):
		"""
		Parses a whole line into input, output and optional label
		
		@type	line:	string
		@param	line:	input line
		
		@type 	delimiter:	char
		@param	delimiter:	splits the different data
		"""
		splt = line.split(delimiter)
		inVec = self._parseVec(splt[0])
		outVec = self._parseVec(splt[1])
		if (len(splt) == 2):
			label = ""
		else:
			label = splt[2]
		self.data.append({'in':inVec, 'out':outVec, 'label':label})
		
	def reset(self):
		"""
		resets the data pointer
		"""
		self.index = 0
	
	def next(self):
		"""
		sets the pointer to the next data record
		
		@rtype:	boolean
		@return: True, if more records are available
		"""
		self.index += 1
		return not self.eof()
		
	def eof(self):
		"""
		checks if the more records are available
		
		@rtype:	boolean
		"""
		return self.index == len(self.data)
	
	def getInput(self):
		"""
		@rtype: list
		@return: input
		"""
		return self.data[self.index]['in']
	
	def getOutput(self):
		"""
		@rtype: list
		@return: output
		"""
		return self.data[self.index]['out']
		
	def getLabel(self):
		"""
		@rtype: string
		@return: label
		"""
		return self.data[self.index]['label']

	def convert2Vec(self, data, vec):
		"""
		converts a data list into a data vector
		
		@type	data:	list
		@param	data:	data list
		
		@type	vec:	vectortype
		@param	vec:	data vectortype
		
		@rtype: vector
		"""
		if (type(vec) == c_int):
			return c_int(data[0])
		if (type(vec) == c_float):
			return c_float(data[0])
		for i in range(0, len(vec)):
			vec[i] = data[i]
		return vec
			
	def convertInput2Vec(self, vec):
		"""
		converts the input data into an inputVector
		
		@type	vec: vectortype
		
		@rtype: vector
		"""
		return self.convert2Vec(self.getInput(), vec)
		
	def convertOutput2Vec(self, vec):
		"""
		converts the input data into an outputVector
		
		@type	vec: vectortype
		
		@rtype: vector
		"""
		return self.convert2Vec(self.getOutput(), vec)
		