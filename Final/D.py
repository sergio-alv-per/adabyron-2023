# Lemos o numero de casos de proba
N = int(input())

for _ in range(N):
    empeza = input()
    fila1 = input().split()
    fila2 = input().split()
    fila3 = input().split()

    numX = 0
    numO = 0

    # Contamos o numero de X e O
    for i in fila1+fila2+fila3:
        if i == "X":
            numX += 1
        elif i == "O":
            numO += 1

    # Analizamos os casos no que o numero de X ou O esta desbalanceado
    # tendo en conta quen empeza
    if empeza == "X" and ((numX-numO) > 1 or (numX-numO) < 0):
        print("IMPOSIBLE")
        continue
    elif empeza == "O" and ((numO-numX) > 1 or (numO-numX) < 0):
        print("IMPOSIBLE")
        continue

    # Analizamos se hai tres en raia de X ou O
    raiaX = False
    raiaO = False

    # Tres en raia na primeira diagonal, na primeira fila ou na primeira columna
    if fila1[0] != "." and ((fila1[0] == fila2[0] == fila3[0]) or (fila1[0] == fila1[1] == fila1[2]) or (fila1[0] == fila2[1] == fila3[2])):
        if fila1[0] == "X":
            raiaX = True
        else:
            raiaO = True
    # Tres en raia na columna central
    if fila1[1] != "." and (fila1[1] == fila2[1] == fila3[1]):
        if fila1[1] == "X":
            raiaX = True
        else:
            raiaO = True
    # Tres en raia da terceira columna ou da segunda diagonal
    if fila1[2] != "." and ((fila1[2] == fila2[2] == fila3[2]) or (fila1[2] == fila2[1] == fila3[0])):
        if fila1[2] == "X":
            raiaX = True
        else:
            raiaO = True
    # Tres en raia da segunda fila
    if fila2[0] != "." and (fila2[0] == fila2[1] == fila2[2]):
        if fila2[0] == "X":
            raiaX = True
        else:
            raiaO = True
    # Tres en raia da terceira fila
    if fila3[0] != "." and fila3[0] == fila3[1] == fila3[2]:
        if fila3[0] == "X":
            raiaX = True
        else:
            raiaO = True

    # No caso de que haxa tres en raia das X e das O a vez non e posible
    if raiaX and raiaO:
        print("IMPOSIBLE")
    # Analizamos se o tres en raia das X e valido
    elif raiaX:
        if empeza == "X" and numX-numO == 1:
            print("GANA X")
        elif empeza == "O" and numX-numO == 0:
            print("GANA X")
        else:
            print("IMPOSIBLE")
    # Analizamos se o tres en raia das O e valido
    elif raiaO:
        if empeza == "O" and numO-numX == 1:
            print("GANA O")
        elif empeza == "X" and numO-numX == 0:
            print("GANA O")
        else:
            print("IMPOSIBLE")
    # Miramos se hai empate e, senon, comprobamos quen sigue
    else:
        if numX + numO == 9:
            print("EMPATE")
        elif numX > numO:
            print("SIGUE O")
        elif numO > numX:
            print("SIGUE X")
        # Neste caso estan empatados a pezas e continua o que empeza
        elif empeza == "X":
            print("SIGUE X")
        else:
            print("SIGUE O")
