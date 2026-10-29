tabla = [
    ["Nombre","Edad", "Calificacion"],
    ["Jimena",16,8.0],
    ["Mari",15,8.3],
    ["Amanda",16,8.0],
    ["Sherlyn",16,9.9],
    ["Cecilia",15,8.0],
    ["Litzy",15,7.9],
    ["Ivan",16,7.9],
    ["Ivone",16,9.9],
    ["Pedro",17,7.5],
    ["Sofia",16,7.5]
]
Nombre = input("Escrive tu Nombre:")
filas=len(tabla)
columnas=len(tabla[0])
for i in range(filas):
    for j in range(columnas):
        if tabla[i][j]== Nombre:
             print(f"Nombre encontrado en la posicion [{i}][{j}]")
