num = int(input('Escreva um número inteiro: '))
print('''Escolha qual será a base de conversão de seu número:
[ 1 ] para binário
[ 2 ] para octal
[ 3 ] para hexademal''')
opção = int(input('Sua opção: '))
if opção == 1:
    print(bin(num))
elif opção == 2:
    print(oct(num))
elif opção == 3:
    print(hex(num))
else:
    print('Opção inválida.')
