n = int(input())

botes = []
for i in range(n):
    botes.append(int(input()))

print(max(botes)-min(botes))