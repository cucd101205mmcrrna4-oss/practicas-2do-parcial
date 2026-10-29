#Crear una matriz
letras = [
    ['A', 'B', 'C', 'D', 'E'],
    ['F', 'G', 'H', 'I', 'J'],
    ['K', 'L', 'M', 'N', 'Ñ'],
    ['O', 'P', 'Q', 'R', 'S'],
    ['T', 'U', 'V', 'W', 'X'],
    ['Y', 'Z']
]
for i in range(0,9):
    # Ciclo interno para recorrer las columnas
    for j in range(0,3):
        print(f"[{i}][{j}] = {letras[i][j]}")