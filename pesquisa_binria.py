def pesquisa_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1
    tentativas = 1

    while baixo <= alto:
        # Round para arredondar numeros float
        meio = round((baixo + alto) / 2)
        chute = lista[meio]

        if chute == item:
            return meio
        elif chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1

        tentativas += 1

    return None


minha_lista = [1, 3, 5, 7, 9]

print("3 - Posição: ", pesquisa_binaria(minha_lista, 3))
print("-1 - Posição: ", pesquisa_binaria(minha_lista, -1))
