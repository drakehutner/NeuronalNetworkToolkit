/**
 * FH Wedel, Wintersemester 2010/2011
 * Softwareprojekt: Neuronal Net Toolkit
 * File: weightList.cpp
 *@author: Hanno Sternberg <Tinf6667>
 *
 * Demo Network
 * OO-List for neural connection
 *@author Hanno Sternberg <tinf6667>
 */
using namespace std;

#include <cstddef>
#include "weightList.h"

weightList::weightList(Neuron * n, float w, weightList * l)
{
	this->element = n;
	this->weight = w;
	this->next = l;
}

weightList::~weightList(void)
{
	if (this->next != NULL)
		delete this->next;
}

weightList * weightList::getNext(void)
{
	return this->next;
}

Neuron * weightList::getNeuron(void)
{
	return this->element;
}

float weightList::getWeight(void)
{
	return this->weight;
}

void weightList::setWeight(float newWeight)
{
	this->weight = newWeight;
}
