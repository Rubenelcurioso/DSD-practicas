
struct VECTOR3D{
	float x;
	float y;
	float z;
};

struct vectores3d{
	VECTOR3D vector1;
	VECTOR3D vector2;
};

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

program CALCULADORA_VECTORIAL {
	version AVANZADA_1 {
		float PRODUCTO_ESCALAR(vectores3d) = 1;
		VECTOR3D PRODUCTO_ESCALAR(vectores3d) = 2;
	} =1;
} = 0x20001024;
