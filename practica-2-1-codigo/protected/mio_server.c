/*
 * This is sample code generated by rpcgen.
 * These are only templates and you can use them
 * as a guideline for developing your own functions.
 */

#include "mio.h"

float *
suma_1_svc(operandos arg1,  struct svc_req *rqstp)
{
	static float  result;

	result=arg1.operando1+arg1.operando2;

	return &result;
}

float *
resta_1_svc(operandos arg1,  struct svc_req *rqstp)
{
	static float  result;

	result=arg1.operando1-arg1.operando2;

	return &result;
}

float *
multiplica_1_svc(operandos arg1,  struct svc_req *rqstp)
{
	static float  result;

	result=arg1.operando1*arg1.operando2;

	return &result;
}

float *
divide_1_svc(operandos arg1,  struct svc_req *rqstp)
{
	static float  result;

	result=arg1.operando1/arg1.operando2;

	return &result;
}
