#ifndef __DEMO_H__
#define __DEMO_H__ 1
/**
 * FH Wedel, Wintersemester 2010/2011
 * Softwareprojekt: Neuronale Netze Toolkit
 *
 * Demo Network
 *@author Hanno Sternberg <tinf6667>
 */

#include "net.h"

#include <windows.h>
#define DLL   extern "C" __declspec(dllexport)

DLL int init(void); 

DLL int saveState(char *filename);

DLL int loadState(char *filename);

DLL int inputData(float *inputVector);

DLL int process(void);

DLL int getVector(float *output);

DLL int process(void);

DLL int getNeuron(int index, NeuronName * name, NeuronName * links, float * weights, int linkcnt);

DLL int cleanup(void);



#endif
