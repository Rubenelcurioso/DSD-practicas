struct operandos{
	float operando1;
	float operando2;
};

program CALCULADORA_BASICA {
	version BASICA_1 {
		float SUMA(operandos) = 1;
		float RESTA(operandos) = 2;
		float MULTIPLICA(operandos) = 3;
		float DIVIDE(operandos) = 4;
	} =1;
} = 0x20000001;

