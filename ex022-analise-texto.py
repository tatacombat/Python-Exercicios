nome = str(input('Qual seu nome completo: ')).strip() #.strip vai elimitar espaços em branco antes e depois
print('Tudo maiúsculo: {}'.format(nome.upper()))
print('Tudo minúsculo: {}'.format(nome.lower()))
lista = nome.split()
print('O nome completo possui {} letras'.format(len(nome) - nome.count(' ')))
print ('Seu primeiro nome tem {} letras'.format(nome.find(' ')))