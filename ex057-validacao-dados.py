sexo = str(input('Qual o seu sexo [F/M]: ')).upper()[0].strip()
while sexo not in 'FfMm':
    sexo = str(input("Dados inválidos. Por favor, informe seu sexo: ")).strip().upper()[0]
print('Sexo {} registrado com sucesso.'.format(sexo))
