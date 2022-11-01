imovel = float(input('Qual o valor do imóvel? R$'))
sal = float(input('Qual é o seu salário? R$'))
tempo = int(input('Quantos anos de financiamento? '))
prestação = imovel/(tempo*12)
print('Para pagar uma casa de {:.2f} em {} anos, a prestação será de R${:.2f}'.format(imovel, tempo, prestação))
if prestação > (sal * 0.3):
    print('\33[1;31mEmpréstimo NEGADO!')
else:
    print('\33[1:36mEmpréstimo CONCEDIDO!')
    