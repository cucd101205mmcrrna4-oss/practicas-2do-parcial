#creando una tupla de coordenadas
coordenadas=(10.5,20.3,30.5,10.5)#tupla americana
nombres=("Luis","Ana","Angel")#tupla de cadena de texto
coordenadas[0]=10.9
for indice,coordenada in enumerate(coordenadas):
    print(f"[{indice}]---coordenada[{coordenada}]")


