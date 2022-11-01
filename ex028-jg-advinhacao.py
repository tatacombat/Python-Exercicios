from random import choice
from time import sleep
print('--'*30)
print('Vou pensar em um número de 0 a 5. Tente adivinhar! ')
print('--'*30)
lista = [0, 1, 2, 3, 4, 5]
escolha = choice(lista)
n1 = int(input('Em que número pensei? '))
print('PROCESSANDO...')
sleep(3)
if n1 == escolha:
    print('PARABÉNS! Você me venceu!')
else:
    print('GANHEI!Eu pensei no número {} e não no número {}.'.format(escolha, n1))
print('-----------FIM----------')

#from random import randint
#computador = randint(0, 5) *faz o computador 'pensar'
#print('-=-'*20)
#print('Vou pensar em um número entra 0 e 5. Tente advinhar...')
#print('-=-'*20)
#jogador = int(input(('Em que número pensei? '))
#if jogador == computador:
    #print('Parabéns! Você conseguiu me vencer!')
#else:
    #print('Ganhei! Eu pensei no número {} e não no {}!'.format(computador, jogador))