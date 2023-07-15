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


# Se aplica el algoritmo A*.
nodos_por_procesar = {(0,0): {"posicion": (0,0), "g":vida_perdida[0][0], "h":0, "f":0}}
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

# Aplicación de A*
while nodos_por_procesar and not existe_camino:
    posicion_actual, nodo_actual = min(nodos_por_procesar.items(), key=lambda x: x[1]["f"])
    del nodos_por_procesar[posicion_actual]

    for posicion_siguiente in sucesores(nodo_actual["posicion"]):
        nodo_siguiente = {}
        nodo_siguiente["posicion"] = posicion_siguiente
        nodo_siguiente["g"] = nodo_actual["g"] + vida_perdida[posicion_siguiente[0]][posicion_siguiente[1]]

        if vida_heroe - nodo_siguiente["g"] <= 0:
            # Si el héroe pierde toda su vida al tomar este camino, se descarta
            # el nodo.
            continue
        elif posicion_siguiente == (r-1, c-1):
            # Se ha llegado a la habitación final y el héroe sigue vivo.
            # Se tiene que existe un camino.
            existe_camino = True
            break
        else:
            # Se calcula la heurística para este nodo
            nodo_siguiente["h"] = ((r-1 - posicion_siguiente[0]) + (c-1 - posicion_siguiente[1])) * minima_vida_perdida_inf_der[posicion_siguiente[0]][posicion_siguiente[1]]
            nodo_siguiente["f"] = nodo_siguiente["g"] + nodo_siguiente["h"]

            # Se poda el nodo si ya se ha llegado a esta posición con mejor f
            if posicion_siguiente in nodos_por_procesar and nodos_por_procesar[posicion_siguiente]["f"] <= nodo_siguiente["f"]:
                continue
            if posicion_siguiente in nodos_procesados and nodos_procesados[posicion_siguiente] <= nodo_siguiente["f"]:
                continue
            else:
                # Si no se poda el nodo, se añade a los nodos por procesar
                nodos_por_procesar[posicion_siguiente] = nodo_siguiente
    
    nodos_procesados[nodo_actual["posicion"]] = nodo_actual["f"]

if existe_camino:
    print("yes")
else:
    print("no")
