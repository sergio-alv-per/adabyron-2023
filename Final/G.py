from copy import deepcopy

def obtener_adyacentes(actual, filas, columnas):
    adyacentes = []
    f,c = actual
    if f > 0:
        adyacentes.append((f-1, c))
    if c < columnas-1:
        adyacentes.append((f,c+1))
    if f < filas-1:
        adyacentes.append((f+1,c))
    if c > 0:
        adyacentes.append((f,c-1))
    
    return adyacentes


N = int(input())

for _ in range(N):
    filas, columnas = [int(x) for x in input().split(" ")]

    if filas == 1 and columnas == 1:
        print(input())
        continue
    
    flores = []

    for _ in range(filas):
        flores.append([int(x) for x in input().split(" ")])
    
    
    
    maximo_global = 0

    for f in range(filas):
        for c in range(columnas):
            # empezar en flor f c

            if flores[f][c] == 0:
                continue
            
            copia_flores = deepcopy(flores)

            actual = (f,c)

            polen_recolectado = 0

            while actual != -1:
                polen_recolectado += copia_flores[actual[0]][actual[1]]
                copia_flores[actual[0]][actual[1]] = 0

                adyacentes = obtener_adyacentes(actual, filas, columnas)

                max_adyacente = -1
                max_polen_adyacente = 0

                for a_x, a_y in adyacentes:
                    if copia_flores[a_x][a_y] > max_polen_adyacente:
                        max_adyacente = (a_x, a_y)
                        max_polen_adyacente = copia_flores[a_x][a_y]
                
                actual = max_adyacente
            
            maximo_global = max(maximo_global, polen_recolectado)
    
    print(maximo_global)



            