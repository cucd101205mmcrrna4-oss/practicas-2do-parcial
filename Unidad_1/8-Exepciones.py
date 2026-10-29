#Ejemplo 1 sin manejode excepciones
try:
    numero1=float(input("ingresa el primer numero:"))
    numero2=float(input("ingresa el segundo numero:"))
    numero1=10
    numero2=5
    resultado=numero1/numero2
    print(resultado)
except ZeroDivisionError:
    print("error no se puede ingresar letras")


