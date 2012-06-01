/**
 * FH Wedel, Wintersemester 2010/2011
 * Softwareprojekt: Neuronale Netze Toolkit
 *
 * Demo Net
 *@author Hanno Sternberg <tinf6667>
 */
using namespace std;
#include <cstddef>
#include "Net.h"
 
/**
 *@var Array of string containing the names of the neurons
 */
NeuronName neuronnames[NEURONCOUNT] = {
	"INPUT_1", 	"INPUT_2", 	"INPUT_3", 	"INPUT_4", 	"INPUT_5", 				//Input layer
	"AND", 		"OR", 		"XOR", 		"ANDid", 	"ORid", 	"XORid",	//1. Layer
	"isAND", 	"isOR", 	"isXOR", 	"hasErr",							//2. Layer
	"Y", 		"E"															//Output Layer
}; 
 
Net::Net(void)
{
	/* NEURONS */
	for (int i = 0; i < NEURONCOUNT; i++)
		this->neurons[i] = new Neuron(neuronnames[i]);
	
	/* CONNECTIONS */
	//Input layer
	//1. layer
	//AND
	this->neurons[5]->link(this->neurons[0], 0.2f);
	this->neurons[5]->link(this->neurons[1], 0.2f);
	//OR
	this->neurons[6]->link(this->neurons[0], 0.3f);
	this->neurons[6]->link(this->neurons[1], 0.3f);
	//XOR
	this->neurons[7]->link(this->neurons[0], 0.5f);
	this->neurons[7]->link(this->neurons[1], 0.5f);
	//andId
	this->neurons[8]->link(this->neurons[2],0.5f);
	//orId
	this->neurons[9]->link(this->neurons[3],0.5f);
	//xorId
	this->neurons[10]->link(this->neurons[4],0.5f);
	
	//2. layer
	//isAND
	this->neurons[11]->link(this->neurons[5],0.2f);
	this->neurons[11]->link(this->neurons[8],0.2f);
	//isOR
	this->neurons[12]->link(this->neurons[6],0.2f);
	this->neurons[12]->link(this->neurons[9],0.2f);
	//isXOR
	this->neurons[13]->link(this->neurons[7],0.2f);
	this->neurons[13]->link(this->neurons[10],0.2f);
	//hasError
	this->neurons[14]->link(this->neurons[8],0.2f);
	this->neurons[14]->link(this->neurons[9],0.2f);
	this->neurons[14]->link(this->neurons[10],0.2f);
	
	//Output layer
	//result
	this->neurons[15]->link(this->neurons[11],0.5f);
	this->neurons[15]->link(this->neurons[12],0.5f);
	this->neurons[15]->link(this->neurons[13],0.5f);
	//error
	this->neurons[16]->link(this->neurons[14],0.5f);
}
 
Net::~Net(void)
{
	for(int i = 0; i < 17; i++)
		delete this->neurons[i];
}

void Net::setInput(InputVector input)
{
	for(int i = 0; i < 5; i++)
		this->neurons[i]->setInput(input[i]);
}

void Net::readOutput(OutputVector output)
{
	output[0] = this->neurons[15]->getOutput();
	output[1] = this->neurons[16]->getOutput();
}

void Net::process(void)
{
	for(int i = 0; i < 17; i++)
		this->neurons[i]->process();
}

Neuron * Net::getNeuron(unsigned int index)
{
	if (index < NEURONCOUNT)
		return this->neurons[index];
	else
		return NULL;
}

