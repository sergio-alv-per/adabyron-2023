LOCALIZACION_WA = []

def veredicto(n_inf, n_sup, tope=False):
    if len(LOCALIZACION_WA) <= 3:
        print(f"? {n_inf} {n_sup}")
        respuesta = input()

        if respuesta == "WA":
            if n_inf == n_sup:
                # encontramos un wa
                LOCALIZACION_WA.append(n_inf)
                if len(LOCALIZACION_WA) > 3:
                    # HAY MÁS DE 3 WA
                    print("Veredicto: WA")
            else:
                medio = (n_inf + n_sup)//2
                veredicto(n_inf, medio)
                veredicto(medio+1, n_sup)

        elif respuesta == "AC" and tope:
            print("Veredicto: AC")

n_max = int(input())

while n_max != 0:

    veredicto(1, n_max, tope=True)

    if len(LOCALIZACION_WA) > 0 and len(LOCALIZACION_WA) <= 3:
        print("Veredicto: WA en " + " ".join([str(x) for x in LOCALIZACION_WA]))
    
    LOCALIZACION_WA = []

    n_max = int(input())

