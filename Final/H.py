# A solucion abordada consiste en calcular o maximo numero de 
# lapices que forman unha recta que pertence ao convex-hull que 
# se obten ao ter en conta as alturas dos lapices como puntos
# de R2
# Para iso percorremos os lapices (de esquerda a dereita) buscando
# a recta de maxima pendente que une ese lapiz cos que estan a sua dereita
# e contando os lapices que forman esta recta de maxima pendente
#
# A solucion e de orde O(n^2)

# leemos el numero de casos de prueba
N = int(input())

for _ in range(N):
    # Leemos el numero de lapices del lapicero
    n_lapices = int(input())
    lapicero = [int(i) for i in input().split()]

    p1 = 0
    v1 = lapicero[0]

    # Neste caso so hai un lapiz e o resultado e obvio
    if p1 == n_lapices-1:
        max_puntos_recta = 1
    else:
        max_puntos_recta = 0
    
    # Recorremos los lapices del lapicero en orden de izquierda a derecha
    # Para cada lapiz, recorreremos el lapicero hacia la derecha buscando los
    # lapices que determinan una recta (junto con el actual) que determinan
    # la recta de maxima pendiente
    while p1 != (n_lapices-1):
        # Leemos el siguiente lapiz del lapicero
        pendente_max = lapicero[p1+1]-v1
        # Contamos el numero de lapices que forman parte de la recta de maxima pendiente
        n_lapices_recta = 2
        # El ultimo lapiz de la recta sera el siguiente lapiz a analizar
        ultimo_lapiz_recta = p1+1

        # Recorremos los siguientes lapices
        for p2, v2 in enumerate(lapicero[p1+2:], start=p1+2):
            pendente = (v2-v1)/(p2-p1)
            # Encontramos una recta con mas pendiente
            if pendente > pendente_max:
                pendente_max = pendente
                n_lapices_recta = 2
                ultimo_lapiz_recta = p2
            # En este caso anhadimos un lapiz a la recta
            elif pendente == pendente_max:
                n_lapices_recta += 1
                ultimo_lapiz_recta = p2

        # Vamos la variable que almacena la recta con mas lapices
        if n_lapices_recta > max_puntos_recta:
            max_puntos_recta = n_lapices_recta
        
        # El siguiente a analizar sera el ultimo lapiz de la recta
        # de maxima pendiente
        # De este modo no analizamos los puntos que ya forman parte de una
        # recta ni los lapices que no forman parte del convex-hull
        p1 = ultimo_lapiz_recta
        v1 = lapicero[p1]

    print(max_puntos_recta)
           

