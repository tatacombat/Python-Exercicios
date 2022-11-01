from datetime import date
nasc = int(input('Qual seu ano de nascimento? '))
atual = date.today().year
idade = atual - nasc
if idade == 18:
    print('Está na hora de se alistar!')
elif idade < 18:
    print('Calma, ainda falta {} anos para você se alistar.'.format(18 - idade))
else:
    print('Já passou do tempo de se Alistar. Deveria ter se alistado há {} anos'.format(idade - 18))
