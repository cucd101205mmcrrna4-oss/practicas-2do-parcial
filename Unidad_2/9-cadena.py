#Cadenas y concatenacion con (+)
cadena1='Hola '
cadena2='Mundo '
Multilinea=""" Esto es una cadena 
de varias lineas"""
print(cadena1 + cadena2 + Multilinea)#print(f("{cadena1}"))
#Cadenas y repeticion 
eco='ja'*3
print(eco)
#cambiar cadenas de minusculas a mayusculas 
tu_nombre='Diana'
print(tu_nombre.upper())
#cambiar cadenas de mayusculas a minuscula 
print(tu_nombre.lower())
#Remplasar texto a una cadena 
frase="Me gusta programacion"
print(frase.replace("programacion","el frio"))
#formato de cadenas(F-String)
edad=15
nombre='Diana'
Mensaje=f'Hola, me llamo {nombre}\ny tengo {edad}años'
print(Mensaje)
#Encontrar los caracteres de una cadena 
texto="¡Felicidades por aun continuar en el CECY!!!"
cantidad_caracteres=len(texto)
print(cantidad_caracteres)
#comprobar si un texto contiene una palabra
oracion="Aprender python es divertido"
if "Java" in oracion:
    print("Encontrado")
else:
    print ("No esta")
#validar contenido de una cadena 
nlista="5"
print(nlista.isalpha())
print(nlista.isdigit())


