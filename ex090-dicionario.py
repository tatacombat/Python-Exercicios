aluno = dict()
aluno['Nome'] = str(input('Nome do Aluno: '))
aluno['Media'] = float(input(f'Média de {aluno["Nome"]}: '))
print(f'O aluno {aluno["Nome"]} tem média igual a {aluno["Media"]}.')
if aluno['Media'] >= 7:
    print(f'O aluno {aluno["Nome"]} foi APROVADO.')
elif 5 <= aluno['Media'] < 7:
    print(f'O aluno {aluno["Nome"]} está em RECUPERAÇÃO.')
else:
    print(f'O aluno {aluno["Nome"]} foi REPROVADO.')
