dist = float(input('Qual é a distância da sua viagem? '))
print('Você está prestas a começar uma viagem de {}km'.format(dist))
if dist <= 200:
    preço = dist * 0.50
else:
    preço = dist * 0.45
print ('E o preço da sua passagem sera´de R${:.2f}'.format(preço))
