def mensagem(txt):
    t = len(txt) + 4
    print('~' * t)
    print(f'{txt:^{t}}')
    print('~' * t)


mensagem('Oi')
mensagem('Bem Vindo!')
mensagem('Tchau')
