#------------------------------------------------------------------------------------
# Neuronal Network Toolkit
# 
# Hanno Sternberg <hanno@almostintelligent.de>
# 
# makefile 
#	- compiles libraries
#	- test
#	- cleanup
# 
#------------------------------------------------------------------------------------
CC=g++
CCFLAGS=-c -O0 -DMAKEDLL
DOT=dot
DOC=epydoc.py

all: lib test

all-vs: lib-vs test

Demo: demoDLL test-NNT

#build all libs
lib: demoDLL

# create png using graphviz
%.png: %.gv
	@$(DOT) -Tpng -O $< 
	
# compile sourcecode
%.o: %.cpp
	$(CC) $(CCFLAGS) -o $@ $< 
%.dll:
	$(CC) -shared -o $@ $<

#demo net
DEMOSRC=../libs/Demo/weightList.cpp ../libs/Demo/Neuron.cpp ../libs/Demo/Net.cpp ../libs/Demo/demo.cpp
DEMOOBJ=$(DEMOSRC:.cpp=.o)
demoDLL: $(DEMOOBJ)
	$(CC) -shared -o demo.dll $(DEMOOBJ)
	

# start python
start:
	@Python

# Basic function test for the toolkit
test-NNT:
	@echo "Test Toolkit"
	@Python TestNNT.py > TestNNT_01.log
	@DOT -Tpng -oout/DemoVis.png out/demo.gv


# all tests
test: test-NNT
	
#doc
doc:
	$(DOC) -v --config epydoc.cfg
	
#cleanup
clean-test:
	@echo "cleanup test directory"
	@rm -rf out/
	@mkdir out
	@rm -f *.log

clean-demo:
	@echo "cleanup demo binaries"
	@rm -f ../libs/Demo/*.o
	@rm -f ../libs/Demo/*.bak
	
	
clean-py:
	@echo "cleanup python binaries"
	@rm -f NNT/*.pyc
	@rm -f NNT/NetLoader/*.pyc
	@rm -f NNT/Visualizer/*.pyc

	
clean: clean-py clean-demo clean-test 
	
clean-all: clean
