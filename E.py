import itertools

n_en_mano = int(input())
m_en_mesa = int(input())

en_mano = []
for _ in range(n_en_mano):
    carta = input()
    num = int(carta[:-1])
    if num > 9:
        num = num-2
    en_mano.append((num, carta))

en_mesa = []
for _ in range(m_en_mesa):
    carta = input()
    num = int(carta[:-1])
    if num > 9:
        num = num-2
    en_mesa.append((num, carta))

combinaciones = []
for i in range(1,m_en_mesa+1):
    combinaciones += list(itertools.combinations(en_mesa, i))


baza_mano = ""
baza_mesa = []
valor_maximo = 0

se_puede_coger = False
for valor, carta in en_mano:
    objetivo = 15-valor
    for c in combinaciones:
        suma = sum([x[0] for x in c])
        if suma == objetivo:
            se_puede_coger = True
            num_cartas_tomadas = len(c)+1
            if num_cartas_tomadas > valor_maximo:
                valor_maximo = num_cartas_tomadas
                baza_mano = carta
                baza_mesa = [x[1] for x in c]

if not se_puede_coger:
    print("NOSOL")
else:
    print(baza_mano)
    print(" ".join(sorted(baza_mesa)))