n, t_casa = [int(x) for x in input().split(" ")]

while n != 0 or t_casa != 0:

    horarios = []

    for _ in range(n):
        dia1, hora1, dia2, hora2 = input().split(" ")

        hora1, min1 = hora1.split(":")

        hora2, min2 = hora2.split(":")

        t_entrada = int(min1) + int(hora1) * 60 + int(dia1) * 24 * 60

        t_salida = int(min2) + int(hora2) * 60 + int(dia2) * 24 * 60

        horarios.append((t_entrada, t_salida))
    
    horarios = sorted(horarios)

    inicio_bloque = horarios[0][0]
    fin_bloque = horarios[0][1]

    viajes = 1

    for inf,sup in horarios[1:]:
        if inf <= fin_bloque and sup <= fin_bloque:
            continue
        if inf <= fin_bloque and sup > fin_bloque:
            fin_bloque = sup
            continue
        if inf > fin_bloque and inf < fin_bloque + 2*t_casa:
            fin_bloque = sup
            continue
        if inf >= fin_bloque + 2*t_casa:
            viajes +=1
            inicio_bloque = inf
            fin_bloque = sup
    
    print(viajes)
    
    n, t_casa = [int(x) for x in input().split(" ")]