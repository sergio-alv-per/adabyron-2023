from collections import defaultdict
from itertools import combinations, tee

def resolver_2SAT(grafo, traspuesto, n):
    utilizados = set()
    orden = []
    componente = {}
    asignacion = []

    def iterativo1(nodo):
        pila = [(False, nodo)]

        while pila:
            es_padre, nodo =  pila.pop()
            
            if es_padre:
                orden.append(nodo)
            elif nodo in utilizados:
                continue
            else:
                utilizados.add(nodo)
                pila.append((True, nodo))
                for otro in grafo[nodo]:
                    if otro not in utilizados:
                        pila.append((False, otro))

    for nodo in grafo:
        if nodo not in utilizados:
            iterativo1(nodo)
    
    cc = 0
    for nodo in reversed(orden):
        if nodo not in componente:
            pila = [nodo]

            while pila:
                tope = pila.pop()
                if tope not in componente:
                    componente[tope] = cc
                    for otro in traspuesto[tope]:
                        if otro not in componente:
                            pila.append(otro)
            cc += 1
    
    for nodo in range(1, n+1):
        if componente[nodo] == componente[-nodo]:
            return False
        asignacion.append(componente[nodo] > componente[-nodo])
    return asignacion

def obtener_solucion(indice_ultima_puerta, puertas):
    grafo = {**{x:set() for x in range(1, indice_ultima_puerta+1)}, **{-x:set() for x in range(1, indice_ultima_puerta+1)}}
    grafo_t = {**{x:set() for x in range(1, indice_ultima_puerta+1)}, **{-x:set() for x in range(1, indice_ultima_puerta+1)}}
    llaves = defaultdict(set)

    for i, (llaves_izq, llaves_der) in enumerate(puertas[:indice_ultima_puerta], start=1):
        for l in llaves_izq:
            llaves[l].add(-i)
        for l in llaves_der:
            llaves[l].add(i)
    
    for l in llaves:
        for (p1, p2) in combinations(llaves[l], 2):
            # (p1, p2) es un par de puertas que tienen cerradura de la llave l
            # Necesariamente o no se pasa por p1 o no se pasa por p2
            # ¬p1 V ¬p2
            # equivalentemente p1 => ¬p2 y p2 => ¬p1
            grafo[p1].add(-p2)
            grafo[p2].add(-p1)

            grafo_t[-p2].add(p1)
            grafo_t[-p1].add(p2)
    
    asignacion = resolver_2SAT(grafo, grafo_t, indice_ultima_puerta)

    return asignacion


N = int(input())

for _ in range(N):
    n_puertas = int(input())

    puertas = []

    for _ in range(n_puertas):
        llaves_izq = [int(x) for x in input().split(" ")][1:]
        llaves_der = [int(x) for x in input().split(" ")][1:]

        puertas.append((llaves_izq, llaves_der))
    
    lim_inf = 1
    lim_sup = n_puertas

    solucion_maxima = None
    
    while lim_inf <= lim_sup:
        medio = (lim_inf + lim_sup) // 2
        solucion = obtener_solucion(medio, puertas)

        if solucion:
            solucion_maxima = solucion
            lim_inf = medio+1
        else:
            lim_sup = medio-1
    
    print("".join(["D" if b else "I" for b in solucion_maxima]))
    
