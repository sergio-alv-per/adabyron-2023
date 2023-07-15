N = int(input())

alturas = [(i,int(x)) for i,x in enumerate(input().split(" "))]

alturas = sorted(alturas, key=lambda x: x[1], reverse=True)

Q = int(input())
consultas = []

for i in range(Q):
    consultas.append([int(x) for x in input().split(" ")])

respuestas = [-1]*Q
consultas_vivas = set(range(Q))

for pos, altura in alturas:
    consultas_a_borrar = set()
    for j in consultas_vivas:
        if consultas[j][0] <= pos and pos <= consultas[j][1]:
            consultas_a_borrar.add(j)
            respuestas[j] = altura
    consultas_vivas -= consultas_a_borrar

    if not consultas_vivas:
        break

print("\n".join([str(x) for x in respuestas]))