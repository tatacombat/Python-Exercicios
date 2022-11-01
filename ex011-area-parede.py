l = float(input('Largura da Parede: '))
a = float(input('Altura da Parede: '))
print('Sua parede tem s dimensão de {} x {} e sua área é de {}m².'.format(l, a, l*a))
print('Para pintar essa parede, você precisará de {:.2f}L de tinta.'.format((l*a)/2))
