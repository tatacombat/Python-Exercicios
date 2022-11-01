r = float(input('Quanto dinheiro você tem na carteira? R$ '))
dl = float(input('Qual a cotação atual do dólar? US$ '))
print('Com R${:.2f}, você pode comprar U${:.2f}'.format(r, r/dl))
