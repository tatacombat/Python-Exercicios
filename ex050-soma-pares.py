s = 0
for c in range(1, 7):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        s = s + num
print('A soma dos números pares é {}'.format(s))
