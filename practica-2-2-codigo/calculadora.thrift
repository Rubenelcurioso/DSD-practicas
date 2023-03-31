service Calculadora{
   void ping(),
   double suma(1:double num1, 2:double num2),
   double resta(1:double num1, 2:double num2),
   double multiplica(1:double num1, 2:double num2),
   double divida(1:double num1, 2:double num2),
   list<double> suma_vectorial(1:list<double> v1, 2:list<double> v2),
   list<double> resta_vectorial(1:list<double> v1, 2:list<double> v2),
   double   producto_escalar(1:list<double> v1, 2:list<double> v2),
   list<double> producto_vectorial(1:list<double> v1, 2:list<double> v2)
  
}

service Calculadora_avanzada{
   list<double> suma_vectorial(1:list<double> v1, 2:list<double> v2),
   list<double> resta_vectorial(1:list<double> v1, 2:list<double> v2),
   double   producto_escalar(1:list<double> v1, 2:list<double> v2),
   list<double> producto_vectorial(1:list<double> v1, 2:list<double> v2)
}