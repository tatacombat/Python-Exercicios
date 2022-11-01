num = []
par = []
impar = []
while True:
    num.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N]')).upper()
    if resp in 'Nn':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        par.append(v)
    elif v % 2 == 1:
        impar.append(v)
print(f'Lista com valores pares: {par}')
print(f'Lista com valores ímpares: {impar}')
print(f'Lista completa: {num}')
