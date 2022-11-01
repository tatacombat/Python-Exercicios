dias = int(input('Quantos dias ficou com o carro? '))
km = float(input('Quantos quilômetros percorridos? '))
pago = (dias * 60) + (km * 0.15)
print('O valor a ser pago por {} dias com o veículo e {:.0f}km rodados é R${:.2f}'.format(dias, km, pago))
