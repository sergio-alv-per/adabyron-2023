# Filas y columnas de la mazmorra
r, c = [int(x) for x in input().split(" ")]

# Vida del héroe
vida_heroe = int(input())

# Se almacena en una matriz la mazmorra, invirtiendo los valores
# De esta forma, se almacena para cada habitación los puntos de vida
# que perderá el héroe si pasa por ahí. En las habitaciones donde haya
# curas, los valores serán negativos.
# Esto se hace para transformar el problema en uno de minimización: minimizar
# la vida que pierde el héroe
vida_perdida = []
for _ in range(r):
    vida_perdida.append([-int(x) for x in input().split(" ")])

# Caso especial de una mazmorra de una habitación
if r == 1 and c == 1:
    if vida_perdida[0][0] < vida_heroe:
        print("yes")
    else:
        print("no")
    exit()


def adyacentes(i, j):
    s = []
    if i < r-1:
        s.append((i+1, j))
    if j < c-1:
        s.append((i, j+1))
    
    return s

infinito = 10000000
# El grafo tiene una forma muy especial, los vértices solo van de izquierda a
# derecha y de arriba a abajo. Es un grafo dirigido acíclico, su orden topológico
# se obtiene recorriéndolo por filas.
dist = [[infinito for _ in range(c)] for _ in range(r)]

dist[0][0] = vida_perdida[0][0]

for i in range(r):
    for j in range(c):
        for (k, l) in adyacentes(i,j):
            # Para cada habitación adyacente se comprueba su distancia. Si pasar
            # por la habitación i,j da una distancia menor que la registrada hasta
            # ahora Y pasar por ella no supondría la muerte del héroe, se reemplaza
            # la distancia guardada.
            if dist[k][l] > dist[i][j] + vida_perdida[k][l] and dist[i][j] + vida_perdida[k][l] < vida_heroe:
                dist[k][l] = dist[i][j] + vida_perdida[k][l]

# Si se consigue un camino hasta el final, se tendrá que la distancia al último
# vértice será menor que infinito.
if dist[r-1][c-1] < infinito:
    print("yes")
else:
    print("no")
