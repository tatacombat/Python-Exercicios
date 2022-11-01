import math
co = float(input('Valor do cateto oposo: '))
ca = float(input('Valor do cateto adjacente: '))
hi = math.hypot(co, ca)
print(f"O valor da hipotenusa equivale à {hi:.2f}.")
