cadena = input()

pila = []
n_diamantes = 0

for c in cadena:
    if c == "<":
        pila.append("<")
    if c == ">" and pila:
        n_diamantes += 1
        pila.pop()

print(n_diamantes)