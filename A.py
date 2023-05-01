N = int(input())
contribuyentes = [int(x) for x in input().split(" ")]

contribuyentes.sort()

def primer_mayor_igual(inf, sup, objetivo):
    if inf == sup:
        return inf
    
    indice = inf + (sup-inf)//2
    referencia = contribuyentes[indice]

    if referencia > objetivo:
        return primer_mayor_igual(inf, indice, objetivo)
    elif referencia < objetivo:
        return primer_mayor_igual(indice+1, sup, objetivo)
    else:
        while indice > 0 and contribuyentes[indice-1] == objetivo:
            indice -= 1
        
        return indice

Q = int(input())

for c in range(Q):
    bajo, alto = [int(x) for x in input().split(" ")]

    primero_mayor_igual_bajo = primer_mayor_igual(0, N, bajo)

    primero_mayor_alto = primer_mayor_igual(0, N, alto+1)

    print(primero_mayor_alto-primero_mayor_igual_bajo)
