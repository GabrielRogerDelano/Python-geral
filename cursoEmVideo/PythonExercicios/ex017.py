# calcule a hipotenusa com os catetos fornecidos pelo usuário

import math

b = float(input('Digite o cateto oposto : '))
c = float(input('Digite o cateto adjacente : '))

# a = math.pow(b, 2) + math.pow(c, 2)
a = math.hypot(b, c)

# print(math.sqrt(a))
print(a)
