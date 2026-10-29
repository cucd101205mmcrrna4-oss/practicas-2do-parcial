#creando un diccionario
persona={
    "Nombre":"Diana",
    "Edad":15,
    "Profesion":"Programador",
    "Estudiante":True
}
print(persona)
#Accediendo a un valor en especifico
print(persona["Nombre"])
#se puede usar el metodo get()
#es util pero no marca error si el valor no existe 
print(persona.get("Profesion"))
#modificar un valor existente 
persona["Edad"]=16
print(persona["Edad"])
#Agregamos un par (clave:valor)
persona["Ciudad"]="San Pepe Ranch"
print(persona)
#Recorrer un diccionario con un bucle



