from datetime import datetime
cadastro = {}
cadastro['Nome'] = str(input('Nome: '))
ano = int(input('Ano de nascimento: '))
cadastro['Idade'] = datetime.now().year - ano
cadastro['CTPS'] = int(input('Carteira de trabalho: (0 para não tem)'))
if cadastro['CTPS'] != 0:
    cadastro['Contratação'] = int(input('Ano de contratação: '))
    cadastro['Salário'] = int(input('Salário: R$'))
    cadastro['Aposentadoria'] = cadastro['Idade'] + ((cadastro['Contratação'] + 35) - datetime.now().year)
print('-=' * 20)
for k, v in cadastro.items():
    print(f' -{k} tem valor {v}')
