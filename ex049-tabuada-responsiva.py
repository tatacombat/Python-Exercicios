from time import sleep
n = int(input('Digite um número para ver sua tabuada: '))
for c in range (0,11):
    s = n * c
    print(f'{n} X {c} = {s}')
    sleep(0.5)
