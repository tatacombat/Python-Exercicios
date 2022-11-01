altura = float(input('Digite a altura em mt: '))
peso = float(input('Qual seu peso em kg? '))
imc = peso / (altura ** 2)
print('Seu IMC é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso.')
elif 18.5 <= imc < 25:
    print('Peso Ideal.')
elif 25 <= imc < 30:
    print('Sobrepeso.')
elif 30 <= imc < 40:
    print('obesidade.')
else:
    print('Obesidade mórbida.')