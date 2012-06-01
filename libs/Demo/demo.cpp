/**
 * FH Wedel, Wintersemester 2010/2011
 * Softwareprojekt: Neuronale Netze Toolkit
 *
 * Demo Net
 *@author Hanno Sternberg <tinf6667>
 */
using namespace std;
#include "demo.h"
#include "math.h"
#include <iostream>
 
Net * net;

//DLL Head
BOOL __stdcall DllMain( HANDLE H_Module, DWORD DW_ReasFCall, LPVOID LP_Reserved)
{
	switch(DW_ReasFCall)
	{
		case DLL_PROCESS_ATTACH:
		case DLL_THREAD_ATTACH:
		case DLL_THREAD_DETACH:
		case DLL_PROCESS_DETACH:
		break;
	}
	return TRUE;
}

#define EPSILON 0.001
Data Float2Data(float f)
{
	if (fabs(1 - f) <= EPSILON)
		return One;
	if(fabs(0 - f) <= EPSILON)
		return Zero;
	return UnDef;
}

float Data2Float(Data d)
{
	if (d == One)
		return 1.0;
	if (d == Zero)
		return 0.0;
	return -1;
}

 
DLL int init()
{
	net = new Net();
	return 0;
}

DLL int saveState(char *filename)
{
	cout << "Demo net" << endl;
	cout << "Save to file: " << filename << endl;
	return 0;
}

DLL int loadState(char *filename)
{
	cout << "Demo net" << endl;
	cout << "load from file: " << filename << endl;
	return 0;
}

DLL int inputData(float *inputVector)
{
	InputVector input;
	//cout << "Demo net input" << endl;
	for (int i = 0; i < INPUTLEN; i++)
	{
		input[i] = Float2Data(inputVector[i]);
		//cout << i << ":" << input[i] << endl;
	}
	net->setInput(input);
	return 0;
}

DLL int process(void)
{
	net->process();
	return 0;
}

DLL int getVector(float *output)
{
	OutputVector outputVec;
	//cout << "Demo net input" << endl;
	net->readOutput(outputVec);
	for (int i = 0; i < OUTPUTLEN; i++)
	{
		output[i] = Data2Float(outputVec[i]);
	}
	if (outputVec[1] == One)
		return 1;
	else
		return 0;
}

DLL int getNeuron(int index, NeuronName * name, NeuronName * links, float * weights, int linkcnt)
{
	Neuron * n = net->getNeuron(index);
	if (n == NULL)
		return 1;
	NeuronName * l = links;
	float * w = weights;
	int cnt = n->getLinks(links, weights, linkcnt);
	weights = w;
	links = l;
	*name = n->getName();
	return cnt;
}

DLL int cleanup()
{
	delete net;
	return 0;
}
