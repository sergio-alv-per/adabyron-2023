import math

n_paquetes, n_max_actividades = [int(x) for x in input().split(" ")]

try:
    paquetes = sorted([int(x) for x in input().split(" ")])
except EOFError:
    print("0 0")
    exit()

n_actividades_restantes = n_max_actividades

paquetes_borrar = set()

paquetes_no_fallidos = 0
paquetes_completados = 0
for i, n_actividades in enumerate(paquetes):
    if n_actividades_restantes - math.ceil(n_actividades/2) >= 0:
        n_actividades_restantes -= math.ceil(n_actividades/2)
        paquetes_no_fallidos += 1
        if n_actividades == 1:
            paquetes_completados += 1
            paquetes_borrar.add(i)
    else:
        break

if n_actividades_restantes:
    for i, n_actividades in enumerate(paquetes):
        if i not in paquetes_borrar:
            if n_actividades_restantes - math.floor(n_actividades/2) >= 0:
                n_actividades_restantes -= math.floor(n_actividades/2)
                paquetes_completados += 1
            else:
                break

print(n_paquetes - paquetes_no_fallidos, paquetes_completados)