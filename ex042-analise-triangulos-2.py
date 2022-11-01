print('-=-' * 20)
print('Analisador de Triângulos')
print(('-=-' * 20))
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima \33[1;34mPODEM\33[m formar triângulo.')
    if r1 == r2  == r3:
        print('Todos os lados iguais, triângulo EQUILÁTERO.')
    elif r1 == r2 and r1 !=r3 or r1 == r3 and r1 != r2 or r2 == r3 and r2 != r1:
        print('Dois lados iguais. Triângulo ISÓCELES.')
    else:
        print('Todos os lados diferentes. Triângulo ESCALENO')
else:
    print('Não há condição de existir triângulo.')