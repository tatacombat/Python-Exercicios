from datetime import date
atual = date.today().year
nasc = int(input('Ano de Nascimento do atleta? '))
idade = atual - nasc
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('O atleta está na categoria MIRIM.')
elif idade > 9 and idade <= 14:
    print('O atleta está na categoria INFANTIL.')
elif idade > 14 and idade <= 19:
    print('O atleta está na categoria JUNIOR.')
elif idade > 19 and idade <= 25:
    print('O atleta está na categoria SÊNIOR.')
else:
    print('O atleta está na categoria MASTER.')
