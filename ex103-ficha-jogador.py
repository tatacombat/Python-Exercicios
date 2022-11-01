def ficha(jog='<desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')


nome = str(input('Nome do Jogador: '))
gols = str(input('Número de gols: '))
if gols.isnumeric(): #transforma a str gols em numérico para caso não coloque os dados
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    ficha(gol=gols)
else:
    ficha(nome, gols)