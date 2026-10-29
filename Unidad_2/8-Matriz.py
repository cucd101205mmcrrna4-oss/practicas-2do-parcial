#Creando una matriz
numeros=[
    [1,2,3],#fila 0
    [2,3,4],#fila 1
    [5,6,7]# fila 2
]
#Obtener el numero de filas 
filas=len(numeros)#Filas=3
#Obtener el numero de columnas 
columnas=len(numeros[0])
#Ciclo externo para los indices de las filas (i)
for i in range(filas):
    #Ciclo interno para los indices de las columnas(j)
    for j in range(columnas):
        print(f"[{i}][{j}] = {numeros[i][j]}")



