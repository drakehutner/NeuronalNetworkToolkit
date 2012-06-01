#ifndef __NEURON_H__
#define __NEURON_H__ 1
/**
 * FH Wedel, Wintersemester 2010/2011
 * Softwareprojekt: Neuronal Net Toolkit
 *
 * Demo Network
 * 
 *@author Hanno Sternberg <tinf6667>
 */


typedef enum{UnDef = -1, Zero = 0, One = 1} Data;
#include "weightList.h"

typedef char * NeuronName;

class Neuron 
{
	protected:
		NeuronName name;
		weightList * connections;
		Data output, input;	
		float readInput(weightList * l);
		int readLinks(weightList * l, NeuronName * links, float * weights, int linkcnt);
	public:
		Neuron(NeuronName name);
		~Neuron(void);
		void setInput(Data i);
		Data getOutput(void);
		NeuronName getName(void);
		void link(Neuron * n, float weight);
		void process(void);
		int getLinks(NeuronName * links, float * weights, int linkcnt);
};

#endif
