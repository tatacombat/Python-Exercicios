print('-=-' * 40)
print('' * 40)
times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense', 'Atlético', 'Botafogo',
         'Atlético-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport Recife', 'EC Vitória', 'Curitiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')
print('''[ 1 ] Os 5 primeiros times.
[ 2 ] Os últimos 4 colocados.
[ 3 ] Times em ordem alfabética.
[ 4 ] Em que posição está o time da Chapecoense.
[ 5 ] Sair''')
cont1 = 1
cont2 = 20
while True:
    esc = int(input('Escolha qual opção deseja ver? '))
    if esc == 1:
        for c in range(1, 5):
            print(f'{cont1}º colocado: {times[c]}')
            cont1 += 1
    elif esc == 2:
            print(f'Os últimos 4 colocados são colocado: {times[-4:]}')
    elif esc == 3:
        sor = sorted(times)
        print(f'Times em ordem alfabética: {sor}')
    elif esc == 4:
        ind = times.index('Chapecoense')
        print(f'O time da Chapecoense entá na {ind+1} posição.')
    elif esc == 5:
        break
    else:
        print('TENTE NOVAMENTE.')
print('-=-'*10, 'FIM', '-=-'* 10)
