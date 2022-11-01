from random import randint
from time import sleep
def sorteio(lista):
    print('Sorteando valorres: ', end='')
    for i in range(0, 5):
        n = randint(0, 10)
        lista.append(n)
        print(f'{n} ', end='')
        sleep(0.5)
    print('PRONTO')


def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'A soma dos números pares é: {soma}')


numeros = []
sorteio(numeros)
somapar(numeros)
