def fatorial(num=1):
    """
    --> Calcula o fatorial de um número
    :param n: número a ser calculado.
    :return: o valor do fatorial do número n.
    """
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


n = int(input('Digite um número: '))
print(fatorial(n))
help(fatorial)
