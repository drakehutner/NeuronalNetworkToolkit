#ifndef __WEIGHT_LIST_H__
#define __WEIGHT_LIST_H__ 1
/**
 * FH Wedel, Wintersemester 2010/2011
 * Softwareprojekt: Neuronal Net Toolkit
 *
 * Demo Network
 * OO-List for neural connection
 *@author Hanno Sternberg <tinf6667>
 */
 
//Forward declaration
class Neuron;
class weightList;

class weightList
{
		Neuron * element;
		float weight;
		weightList * next;
	public:
		weightList(Neuron * n, float w, weightList * l);
		~weightList(void);
		
		weightList * getNext(void);
		Neuron * getNeuron(void);
		
		float getWeight(void);
		void setWeight(float newWeight);
};

#endif
