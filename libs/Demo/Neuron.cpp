/**
 * FH Wedel, Wintersemester 2010/2011
 * Softwareprojekt: Neuronal Net Toolkit
 *
 * Demo Network
 * OO-List for neural connection
 *@author Hanno Sternberg <tinf6667>
 */
using namespace std;

#include <cstddef>
#include <iostream>

#include "Neuron.h"
 
 
float Neuron::readInput(weightList * l)
{
	if(l != NULL) 
	{
		return l->getWeight() * l->getNeuron()->getOutput() + this->readInput(l->getNext());
	}
	else
	{
		return 0;
	}
}

int Neuron::readLinks(weightList * l, NeuronName * links, float * weights, int linkcnt)
{
	if (linkcnt <= 0)
		return 1;
	if (l == NULL)
		return 0;
	*weights = l->getWeight();
	*links = l->getNeuron()->getName();
	return this->readLinks(l->getNext(),++links,++weights,--linkcnt);
}

Neuron::Neuron(NeuronName name)
{
	this->name = name;
	this->output = Zero;
	this->input = UnDef;
	this->connections = NULL;
}

Neuron::~Neuron(void)
{
	delete this->connections;
}

void Neuron::setInput(Data i)
{
	this->input = i;
}

Data Neuron::getOutput(void)
{
	return this->output;
}

NeuronName Neuron::getName(void)
{
	return this->name;
}

void Neuron::link(Neuron * n, float weight)
{
	this->connections = new weightList(n, weight, this->connections);
}

void Neuron::process(void)
{
	if (this->input == UnDef)
	{
		float val = this->readInput(this->connections);
		if ((val >= 0.25) && (val <= 0.75))
		{
			this->output = One;
		}
		else
		{
			this->output = Zero;
		}
	}
	else
	{
		this->output = this->input;
	}
}

int Neuron::getLinks(NeuronName * links, float * weights, int linkcnt)
{
	return this->readLinks(this->connections, links, weights, linkcnt);
}

