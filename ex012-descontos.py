p = float(input('Qual o valor do produto? R$ '))
x = int(input('Qual o valor do desconto? %'))
d = (p/100)*x
v = p-d
print('O produto que custava R${:.2f}, com {}% de desconto vai custar R${:.2f}.'.format(p, x, v))
