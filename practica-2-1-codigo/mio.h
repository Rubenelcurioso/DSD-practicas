/*
 * Please do not edit this file.
 * It was generated using rpcgen.
 */

#ifndef _MIO_H_RPCGEN
#define _MIO_H_RPCGEN

#include <rpc/rpc.h>


#ifdef __cplusplus
extern "C" {
#endif


struct VECTOR3D {
	float x;
	float y;
	float z;
};
typedef struct VECTOR3D VECTOR3D;

struct vectores3d {
	VECTOR3D vector1;
	VECTOR3D vector2;
};
typedef struct vectores3d vectores3d;

struct operandos {
	float operando1;
	float operando2;
};
typedef struct operandos operandos;

#define CALCULADORA_BASICA 0x20000001
#define BASICA_1 1

#if defined(__STDC__) || defined(__cplusplus)
#define SUMA 1
extern  float * suma_1(operandos , CLIENT *);
extern  float * suma_1_svc(operandos , struct svc_req *);
#define RESTA 2
extern  float * resta_1(operandos , CLIENT *);
extern  float * resta_1_svc(operandos , struct svc_req *);
#define MULTIPLICA 3
extern  float * multiplica_1(operandos , CLIENT *);
extern  float * multiplica_1_svc(operandos , struct svc_req *);
#define DIVIDE 4
extern  float * divide_1(operandos , CLIENT *);
extern  float * divide_1_svc(operandos , struct svc_req *);
extern int calculadora_basica_1_freeresult (SVCXPRT *, xdrproc_t, caddr_t);

#else /* K&R C */
#define SUMA 1
extern  float * suma_1();
extern  float * suma_1_svc();
#define RESTA 2
extern  float * resta_1();
extern  float * resta_1_svc();
#define MULTIPLICA 3
extern  float * multiplica_1();
extern  float * multiplica_1_svc();
#define DIVIDE 4
extern  float * divide_1();
extern  float * divide_1_svc();
extern int calculadora_basica_1_freeresult ();
#endif /* K&R C */

#define CALCULADORA_VECTORIAL 0x20001024
#define AVANZADA_1 1

#if defined(__STDC__) || defined(__cplusplus)
#define PRODUCTO_ESCALAR 1
extern  float * producto_escalar_1(vectores3d , CLIENT *);
extern  float * producto_escalar_1_svc(vectores3d , struct svc_req *);
extern  VECTOR3D * producto_escalar_1(vectores3d , CLIENT *);
extern  VECTOR3D * producto_escalar_1_svc(vectores3d , struct svc_req *);
extern int calculadora_vectorial_1_freeresult (SVCXPRT *, xdrproc_t, caddr_t);

#else /* K&R C */
#define PRODUCTO_ESCALAR 1
extern  float * producto_escalar_1();
extern  float * producto_escalar_1_svc();
extern  VECTOR3D * producto_escalar_1();
extern  VECTOR3D * producto_escalar_1_svc();
extern int calculadora_vectorial_1_freeresult ();
#endif /* K&R C */

/* the xdr functions */

#if defined(__STDC__) || defined(__cplusplus)
extern  bool_t xdr_VECTOR3D (XDR *, VECTOR3D*);
extern  bool_t xdr_vectores3d (XDR *, vectores3d*);
extern  bool_t xdr_operandos (XDR *, operandos*);

#else /* K&R C */
extern bool_t xdr_VECTOR3D ();
extern bool_t xdr_vectores3d ();
extern bool_t xdr_operandos ();

#endif /* K&R C */

#ifdef __cplusplus
}
#endif

#endif /* !_MIO_H_RPCGEN */
