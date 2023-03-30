service Calculadora{
   void ping(),
   void pingOtroServer(),
   i32 suma(1:i32 num1, 2:i32 num2),
   i32 resta(1:i32 num1, 2:i32 num2),
   i32 multiplica(1:i32 num1, 2:i32 num2),
   double divida(1:i32 num1, 2:i32 num2),
   i32   producto_escalar(1:list<i32> v1, 2:list<i32> v2),
   list<i32> producto_vectorial(1:list<i32> v1, 2:list<i32> v2)
}
