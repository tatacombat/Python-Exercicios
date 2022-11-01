n1 = int(input('Primeira nota: '))
n2 = int(input('Segunda nota: '))
média = (n1 + n2)/2
if média >= 7:
    print('Sua média foi de {:.1f}. Você está \33[1;32mAPROVADO\33[m!'.format(média))
elif média < 5:
    print('Sua média foi de {:.1f}. Você está \33[1;31mREPROVADO\33[m!'.format(média))
else:
    print('Sua média foi de {:.1f}. Você está em \33[1;33mRECUPERAÇÃO!\33[m'.format(média))
