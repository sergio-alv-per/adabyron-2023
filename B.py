cadena = input()

mensaje = ""

inicio = 0
fin = 0

vocal_encontrada = False
for i, c in enumerate(cadena):
    if c in "AEIOUaeiou":
        fin = i
        mensaje += "".join(list(reversed(cadena[inicio:fin])))
        mensaje += c
        inicio = i+1
        vocal_encontrada = True

if vocal_encontrada:
    mensaje += cadena[-1:inicio-1:-1]
else:
    mensaje = cadena[-1:0:-1] + cadena[0]

mitad_caracteres = len(mensaje) // 2
impar = len(mensaje) % 2
final = ""

for i in range(mitad_caracteres):
    final += mensaje[i]
    final += mensaje[-1-i]

if impar:
    final += mensaje[mitad_caracteres]

print(final)

