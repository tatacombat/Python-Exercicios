from random import randint
from time import sleep
from operator import itemgetter
rodada = dict()
ranking = list()
print('-=' * 3, 'Valores Sorteados', '-=' * 3)
for c in range(1, 5):
    rodada[f'Jogador {c}'] = randint(1, 6)
for k, v in rodada.items():
    print(f'O {k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(rodada.items(), key=itemgetter(1), reverse=True) #itemgetter 1 para pegar valor e não chave
print('-=' * 3, 'RANKING DOS JOGADORES', '-=' * 3)
for i, v in enumerate(ranking):
    print(f' {i+1}º Lugar: {v[0]} com {v[1]}.')
    sleep(1)
