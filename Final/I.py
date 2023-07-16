# A solucion abordada consiste en calcular os 
# tempos de chegada a meta para cada ciclista 
# (sumar o tempo que tardou o ciclista e o gap 
# multiplicado pola posicion na que saiu o ciclista)
# e despois aplicar o algoritmo mergeSort ao tempo
# que se contan as inversions. 
#
# Cando se fai o merge, se o elemento do subvector dereito
# que se esta analizando e maior que o elemento do subvector
# esquerdo que se esta analizando, producense tantos adiantamentos
# como elementos teña o subvector esquerdo a dereita (incluido el)
# do elemento do subvector esquerdo que se estaba analizando

# Funcion recursiva que conta adiantamentos
def mergeSort(vec, aux, left, right):
    # Devolvemos un 0 cando intentamos partir un vector cun unico elemento
    if left >= right:
        return 0
    
    adiantamentos = 0
    medio = (left + right)//2
    # Calculamos os adiantamentos que se producen ao ordear o subvector esquerdo
    adiantamentos += mergeSort(vec, aux, left, medio)
    # Calculamos os adiantamentos que se producen ao ordear o subvector dereito
    adiantamentos += mergeSort(vec, aux, medio + 1, right)
    # Tamen debemos contabilizar os adiantamentos ao ordear ambos subvectores
    adiantamentos += merge(vec, aux, left, medio, right)

    return adiantamentos


# Funcion que ordea dous subvectores ordeados
def merge(vec, aux, left, medio, right):
    i = left
    j = medio+1
    k = left

    adiantamentos = 0

    # Imos ordeando os dous vectores e contamos as inversions
    # So un dos dous subvectores quedara sen acabar de copiar en aux
    while i <= medio and j <= right:
        if vec[i] <= vec[j]:
            aux[k] = vec[i]
            i+=1
        else:
            aux[k] = vec[j]
            # Todos os elementos a dereita da posicion i e a esquerda da
            # posicion "medio" (incluida) son maiores que o elemento da posicion j
            adiantamentos += (medio + 1) - i
            j+=1
        k+=1

    # Acabamos de copiar o subvector da esquerda
    while i <= medio:
        aux[k] = vec[i]
        i+=1
        k+=1
    
    # Acabamos de copiar o subvector da dereita
    while j <= right:
        aux[k] = vec[j]
        j+=1
        k+=1
    
    # Copiamos o vector auxiliar
    vec[left:right+1] = aux[left:right+1]
    
    return adiantamentos

n_ciclistas, gap = input().split()

n_ciclistas = int(n_ciclistas)
gap = int(gap)

while n_ciclistas != 0 and gap != 0:

    ciclistas = [(pos*gap)+int(valor) for pos, valor in enumerate(input().split())]

    #print(ciclistas)

    aux = [0]*n_ciclistas

    print(mergeSort(ciclistas, aux, 0, n_ciclistas-1))

    n_ciclistas, gap = input().split()

    n_ciclistas = int(n_ciclistas)
    gap = int(gap)