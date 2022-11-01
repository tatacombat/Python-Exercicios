num = [[], []]
valor = 0
impar = []
for c in range(1, 8):
    valor = (int(input(f'Digite o {c}º valor: ')))
    if valor % 2 == 0:
        num[0].append(valor)
    elif valor % 2 == 1:
        num[1].append(valor)
print(f'Lista com valores pares: {sorted(num[0])}.')
print(f'Lista com valores ímpares: {sorted(num[1])}.')
