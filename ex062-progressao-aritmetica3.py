print('='*20)
print('GERADOR DE PA')
print('='*20)
primeiro = int(input('Qual o primeiro termo? '))
razão = int(input('Qual a razão? '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} '.format(termo), end='→')
        termo += razão
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar? '))
print('A progressão foi mostrada com {} termos.'.format(total))
