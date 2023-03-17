/*
 * This is sample code generated by rpcgen.
 * These are only templates and you can use them
 * as a guideline for developing your own functions.
 */


#include "mio.h"

void calculadora_basica_1(char *host, operandos componentes, int operacion)
{
	CLIENT *clnt;
	float *result_1;
	operandos composed = componentes;

#ifndef DEBUG
	clnt = clnt_create(host, CALCULADORA_BASICA, BASICA_1, "udp");
	if (clnt == NULL)
	{
		clnt_pcreateerror(host);
		exit(1);
	}
#endif /* DEBUG */

		
	while(operacion!=0){
		switch (operacion)
		{
		case 1:
			result_1 = suma_1(composed, clnt);
			if (result_1 == (float *)NULL)
			{
				clnt_perror(clnt, "Llamada suma fallida");
			}
			printf("%f+%f=%f\n", composed.operando1, composed.operando2, *result_1);
		break;
		case 2:
			result_1 = resta_1(composed,clnt);
			if (result_1 == (float *)NULL)
			{
				clnt_perror(clnt, "Llamada resta fallida");
			}
			printf("%f-%f=%f\n", composed.operando1, composed.operando2, *result_1);
		break;
		case 3:
			result_1 = multiplica_1(composed,clnt);
			if (result_1 == (float *)NULL)
			{
				clnt_perror(clnt, "Llamada multiplicacion fallida");
			}
			printf("%fx%f=%f\n", composed.operando1, composed.operando2, *result_1);
		break;
		case 4:
			if(composed.operando2==0){
				clnt_perror(clnt,"Ha divido entre 0!");
				break;
			}
			result_1 = divide_1(composed,clnt);
			if (result_1 == (float *)NULL)
			{
				clnt_perror(clnt, "Llamada division fallida");
			}
			printf("%f/%f=%f\n", composed.operando1, composed.operando2, *result_1);
		break;
		default:
			break;
		}
		menu_basic(&operacion,&composed);
	}

#ifndef DEBUG
	clnt_destroy(clnt);
#endif /* DEBUG */
}

void
calculadora_vectorial_1(char *host)
{
	CLIENT *clnt;
	float  *result_1;
	vectores3d producto_escalar_1_arg1;
	VECTOR3D  *result_2;
	vectores3d producto_escalar_1_arg1;

#ifndef	DEBUG
	clnt = clnt_create (host, CALCULADORA_VECTORIAL, AVANZADA_1, "udp");
	if (clnt == NULL) {
		clnt_pcreateerror (host);
		exit (1);
	}
#endif	/* DEBUG */

	result_1 = producto_escalar_1(producto_escalar_1_arg1, clnt);
	if (result_1 == (float *) NULL) {
		clnt_perror (clnt, "call failed");
	}
	result_2 = producto_escalar_1(producto_escalar_1_arg1, clnt);
	if (result_2 == (VECTOR3D *) NULL) {
		clnt_perror (clnt, "call failed");
	}
#ifndef	DEBUG
	clnt_destroy (clnt);
#endif	 /* DEBUG */
}

void menu_basic(int *op, operandos *comp)
{ // Menú interactivo
	printf("\n========Calculadora========\n");
	printf("1. Suma\n");
	printf("2. Resta\n");
	printf("3. Multiplicacion\n");
	printf("4. Division\n");
	printf("\nEscoja una operación = ");
	scanf("%d", &(*op));
	printf("\nIntroduzca los operandos espaciando => ");
	scanf("%f %f", &comp->operando1, &comp->operando2);
}

int main(int argc, char *argv[])
{
	char *host;

	if (argc < 2)
	{
		printf("usage: %s server_host\n", argv[0]);
		exit(1);
	}

	int operacion;
	operandos componentes;
	menu_basic(&operacion, &componentes);

	host = argv[1];
	calculadora_basica_1(host, componentes, operacion);
	calculadora_vectorial_1(host);
	exit(0);
}

