while True:
    n = int(input('Digite um número para saber sua tabuada: '))
    print('-' * 30)
    if n < 0:
        break
    for c in range(1, 11):
        print('{} X {} = {}'.format(n, c, n*c)) # n = numero, c = contador
    print('-' * 30)
print('Programa de tabuada encerrado!')
