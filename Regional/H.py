N = int(input())

intercambios = []

for i in range(N):
    intercambios.append(int(input()))

mejor = 0
actual = 0

for i in intercambios:
    actual = max(actual + i, 0)
    mejor = max(actual, mejor)

print(mejor)