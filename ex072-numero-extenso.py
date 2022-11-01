seq = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
       'seis', 'sete', 'oito', 'nove', 'dez',
       'onze', 'doze', 'treze', 'quatorze',
       'quinze', 'dezesseis', 'dezessete',
       'dezoito', 'dezenove', 'vinte')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if num < 0 or num > 20:
        print('Tente de novo. Digite um número entre 0 e 20: ')
        continue
    if 0 <= num <=20:
        print(f'Você digitou o número {seq[num]}.')
        continuar = str(input('Você quer continuar? [S/N]')).strip().upper()[0]
        if continuar in 'Sn':
            continue
        if continuar in 'Nn':
            print('PROGRAMA ENCERRADO')
            break
