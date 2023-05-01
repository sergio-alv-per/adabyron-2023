import heapq

# Filas y columnas de la mazmorra
r, c = [int(x) for x in input().split(" ")]

# Vida del héroe
v = int(input())

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
    if vida_perdida[0][0] < v:
        print("yes")
    else:
        print("no")
    exit()

# Se genera una matriz para la heurística utilizada en A*, que funciona como una
# caché de valores mínimos. La heurística se basa en multiplicar la distancia
# Manhattan hasta la salida por el valor mínimo de vida perdida que hay entre
# las habitaciones que aún pueden ser visitadas, es decir, aquellas que están
# más abajo y más a la derecha. Se genera esta matriz para almacenar en la
# posición i,j el mínimo de todos los valores de las posiciones k,l con k>= i y
# j >= l. Así, no se tienen que recalcular los máximos cada vez.
minima_vida_perdida_inf_der = [[0 for _ in range(c)] for _ in range(r)]

for i in range(r-1, -1, -1):
    for j in range(c-1, -1, -1):
        if i == r-1 and j == c-1:
            minima_vida_perdida_inf_der[i][j] = vida_perdida[i][j]
        elif i == r-1:
            minima_vida_perdida_inf_der[i][j] = min(vida_perdida[i][j], minima_vida_perdida_inf_der[i][j+1])
        elif j == c-1:
            minima_vida_perdida_inf_der[i][j] = min(vida_perdida[i][j], minima_vida_perdida_inf_der[i+1][j])
        else:
            minima_vida_perdida_inf_der[i][j] = min(vida_perdida[i][j], minima_vida_perdida_inf_der[i][j+1], minima_vida_perdida_inf_der[i+1][j])


# Se aplica el algoritmo A*. Los nodos vivos se almacenan en un montículo,
# ordenado minimizando el valor de f del nodo.
nodos_por_procesar = [(vida_perdida[0][0], 0, {"posicion":(0,0), "g":vida_perdida[0][0], "h":0, "f":0})]
dict_nodos_por_procesar = {(0,0): vida_perdida[0][0]}
nodos_procesados = {}

# Función que devuelve las posiciones a las que puede ir el héroe desde una
# posición dada.
def sucesores(posicion):
    s = []
    if posicion[0] < r-1:
        s.append((posicion[0]+1, posicion[1]))
    if posicion[1] < c-1:
        s.append((posicion[0], posicion[1]+1))
    
    return s


existe_camino = False
# Variable auxiliar para mantener el orden de inserción en el montículo
contador_heap = 1

# Aplicación de A*
while nodos_por_procesar and not existe_camino:
    _, _, q = heapq.heappop(nodos_por_procesar)
    del dict_nodos_por_procesar[q["posicion"]]

    for pos in sucesores(q["posicion"]):
        nodo = {}
        nodo["posicion"] = pos
        nodo["g"] = q["g"] + vida_perdida[pos[0]][pos[1]]

        if v - nodo["g"] <= 0:
            # Si el héroe pierde toda su vida al tomar este camino, se descarta
            # el nodo.
            continue
        elif pos == (r-1, c-1):
            # Se ha llegado a la habitación final y el héroe sigue vivo.
            # Se tiene que existe un camino.
            existe_camino = True
            break
        else:
            # Se calcula la heurística para este nodo
            nodo["h"] = ((r-1 - pos[0]) + (c-1 - pos[1])) * minima_vida_perdida_inf_der[pos[0]][pos[1]]
            nodo["f"] = nodo["g"] + nodo["h"]

            # Se poda el nodo si ya se ha llegado a esta posición con mejor f
            if pos in nodos_por_procesar and nodos_por_procesar[pos] <= nodo["f"]:
                continue
            if pos in nodos_procesados and nodos_procesados[pos] <= nodo["f"]:
                continue
            else:
                # Si no se poda el nodo, se añade al montículo
                heapq.heappush(nodos_por_procesar, (nodo["f"], contador_heap, nodo))
                contador_heap += 1
                dict_nodos_por_procesar[pos] = nodo["f"]
    
    nodos_procesados[q["posicion"]] = q["f"]

if existe_camino:
    print("yes")
else:
    print("no")
