pessoas = list()
dado = list()
maior = menor = 0
while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maior = menor = dado[1]
    else:
        if dado[1] > maior:
            maior = dado[1]
        if dado[1] < menor:
            menor = dado[1]
    pessoas.append(dado[:])
    dado.clear()
    resp = str(input('Quer continuar? [S/N]')).upper()
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'Ao todo cadastramos {len(pessoas)} pessoas.')
print(f'O maior peso foi de {maior:.2f}kg. Peso de ', end='')
for p in pessoas:
    if p[1] == maior:
        print(f'[{p[0]}]')
print(f'O menor peso foi de {menor:.2f}kg. Peso de ', end='')
for p in pessoas:
    if p[1] == menor:
        print(f'[{p[0]}] ')
print('-=' * 30)