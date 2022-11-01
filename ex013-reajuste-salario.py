print('CÁLCULO AUMENTO SALARIAL!')
sal = float(input('Qual é o salário do funcionário?R$ '))
aum = float(input('Qual é a porcentagem do aumento? '))
p = sal * aum / 100
t = sal + p
print('Com um aumento {:.2F}%, o salário terá um acréscimo de R${:.2F}, ficando com um total de R${:.2F}.'.format(aum, p, t))
