num = []
while True:
    num.append(int(input('Digite um valor: ')))
    cont = str(input('Quer continuar? [S/N]')).upper()
    while cont not in 'SsNn':
        cont = str(input('resposta inválida. Quer continuar? [S/N] '))
    if cont in 'Nn':
        break
num.sort(reverse=True)
print('-='*30)
print(f'Você digitou {len(num)} elementos!')
print(f'Os valores em ordem descrescente são {num}.')
if 5 not in num:
    print('O valor 5 não faz parte da lista.')
else:
    print('O valor 5 faz parte da lista.')
