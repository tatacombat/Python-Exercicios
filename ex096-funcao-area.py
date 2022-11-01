def area(l, c):
    s = l * c
    print(f'A área de um terreno {l} x {c} é de {s}m²')


print('-' * 20)
print('Controle de Terrenos')
print('-' * 20)
a1 = float(input('Largura: '))
a2 = float(input('Comprimento: '))
area(a1, a2)
