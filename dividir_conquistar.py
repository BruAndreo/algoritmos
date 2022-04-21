# Exemplo de dividir para conquistar
# Usando uma função de soma de valores de um array

def soma(valores):
    total = 0
    if len(valores) == 1:
        return valores[0]
    else:
        valor = valores.pop(0)
        total = valor + soma(valores)
    return total


print(soma([1, 2, 3, 4, 5, 6]))
