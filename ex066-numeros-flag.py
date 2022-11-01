n = s = v = 0
while True:
    n = int(input('Digite um número: (999 para parar): '))
    if n == 999:
        break
    s += n
    v += 1
print(f'A soma dos {v} valores vale {s}.')
