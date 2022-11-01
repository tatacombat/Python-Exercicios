lista = []
resposta = ''
while resposta in 'Ss':
    num = int(input('Digite um valor: '))
    if num not in lista:
        lista.append(num)
    else:
        print('Esse número já foi adicionado.')
    resposta = str(input('Quer continuar? [S/N]: ')).upper()
    if resposta == 'Nn':
        break
print(f'A lista de números em ordem crescente é {sorted(lista)}')
