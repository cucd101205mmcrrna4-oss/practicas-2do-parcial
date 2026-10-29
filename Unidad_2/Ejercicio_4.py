#El mapa de le tesoro 
mapa=[
    [".",".",".","."],
    [".",".","X","."],
    [".",".",".","."],
    [".",".",".","."]
]
filas=len(mapa)
columnas=len(mapa)
#Recoriendo la matris con ciclos anidados 
#Ciclo externo para manejar filas(i)
for i in range(filas):
    #Ciclo externo para manejar filas(j)
    for j in range(columnas):
        #Verificamos si encotramos el tesoro
        if mapa[i][j] == "x":
             print(f"Mapa encontrado en la posicion [{i}][{j}]")


