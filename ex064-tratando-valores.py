n = cont = soma = 0
n = int(input('Digite um número: '))
while n != 999:
    cont += 1
    soma += n
    n = int(input('Digite um número: '))
print('No total foram {} números digitados e a soma entre eles é {}'.format(cont, soma))
