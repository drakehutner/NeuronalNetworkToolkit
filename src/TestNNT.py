"""
Neuronal Network Toolkit - Example Test

@author: Hanno Sternberg <hanno@almostintelligent.de>

"""

from NNT import NNT

print "NNT basic function test"

toolkit = NNT.Toolkit()
toolkit.init("Demo","")
toolkit.create()
print "create network"

def testVec(vec):
	toolkit.input(vec)
	out = toolkit.output()
	print "\tResult: ", out[0] 
	print "\tError:  ", out[1]



print "1 AND 1"
testVec(toolkit.getInputVector([1,1,1,0,0]))

print "1 OR 1"
testVec(toolkit.getInputVector([1,1,0,1,0]))

print "1 XOR 1"
testVec(toolkit.getInputVector([1,1,0,0,1]))

print "0 AND 1"
testVec(toolkit.getInputVector([0,1,1,0,0]))

print "0 OR 1"
testVec(toolkit.getInputVector([0,1,0,1,0]))

print "0 XOR 1"
testVec(toolkit.getInputVector([0,1,0,0,1]))

print "1 XOR 0"
testVec(toolkit.getInputVector([1,0,0,0,1]))

print "Error"
testVec(toolkit.getInputVector([1,0,0,1,1]))

print "visualize"
toolkit.visualize("out\demo.gv",{'showHead','showLabel'})

print "cleanup network"
toolkit.cleanup()
