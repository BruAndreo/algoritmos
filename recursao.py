def fat(x):
    resultado = 0
    if x == 1:
        resultado = 1
    else:
        resultado = x * fat(x-1)

    print(f"Resultado do fatorial de {x} é {resultado}")
    return resultado


fat(3)
