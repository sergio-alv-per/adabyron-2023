N = int(input())

intercambios = []

for i in range(N):
    intercambios.append(int(input()))

mat = [[-1000000 for _ in range(N)] for _ in range(N)]

for dif in range(0, N):
    for i in range(N-dif):
        j = i+dif
        if dif == 0:
            mat[i][j] = intercambios[i]
        else:
            mat[i][j] = max(mat[i][j-1], mat[i+1][j], sum(intercambios[i:j+1]))

if N:
    print(mat[i][j])