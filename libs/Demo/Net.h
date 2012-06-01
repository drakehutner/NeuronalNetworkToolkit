#ifndef __NETWORK_H__
#define __NETWORK_H__ 1
/**
 * FH Wedel, Wintersemester 2010/2011
 * Softwareprojekt: Neuronal Net Toolkit
 *
 * Demo Network
 *@author Hanno Sternberg <tinf6667>
 */

 
#include "Neuron.h"
#include "weightList.h"

#define NEURONCOUNT 17

#define MAXIMUMLINKS 3

#define INPUTLEN 5
typedef Data InputVector[INPUTLEN];
#define OUTPUTLEN 2
typedef Data OutputVector[OUTPUTLEN];

class Net
{
	Neuron * neurons[NEURONCOUNT];
	
	public:
	Net(void);
	~Net(void);
	void setInput(InputVector input);
	void readOutput(OutputVector output);
	
	void process(void);
	
	Neuron * getNeuron(unsigned int index);
	
};
	


#endif
