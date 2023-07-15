n_elementos, n_reglas = [int(x) for x in input().split(" ")]

mat = [[1000000 for _ in range(n_elementos)] for _ in range(n_elementos)]

for regla in range(n_reglas):
    i, j, coste = [int(x) for x in input().split(" ")]
    mat[i][j] = coste
    mat[j][i] = coste

for i in range(n_elementos):
    mat[i][i] = 0

for k in range(n_elementos):
    for i in range(n_elementos):
        for j in range(n_elementos):
            if mat[i][j] > max(mat[i][k], mat[k][j]):
                mat[i][j] = max(mat[i][k], mat[k][j])

n_consultas = int(input())
n_trans = 0

for c in range(n_consultas):
    i, j, valor = [int(x) for x in input().split(" ")]
    if mat[i][j] <= valor:
        n_trans += 1

print(n_trans)


