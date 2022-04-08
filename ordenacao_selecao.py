def busca_menor(arr):
    menor = arr[0]
    menor_indice = 0
    for i in range(1, len(arr)):
        if arr[i] < menor:
            menor = arr[1]
            menor_indice = i
    return menor_indice


def ordenacao_por_selecao(arr):
    novo_arr = []
    for i in range(len(arr)):
        menor = busca_menor(arr)
        novo_arr.append(arr.pop(menor))
    return novo_arr


print(ordenacao_por_selecao([5, 1, 6, 8, 7, 2, 9, 4, 3, 0]))
