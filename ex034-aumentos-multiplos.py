nome = str(input('Qual o nome do funcionário? '))
sal = float(input('Qual o salário atual de {}?'.format(nome)))
if sal <= 1250:
    novosal = sal + (sal * 15/100)
    print('O novo salário de {} é R${:.2f}'.format(nome, novosal))
else:
    novosal = sal + (sal * 10/100)
    print('O novo salário de {} é R${:.2f}'.format(nome, novosal))
