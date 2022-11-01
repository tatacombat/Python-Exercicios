from random import choice
a = str(input('Nome: '))
b = str(input('Nome: '))
c = str(input('Nome: '))
d = str(input('Nome: '))
lista = [a, b, c, d]
print('O aluno sorteado foi: {}'.format(choice(lista)))
