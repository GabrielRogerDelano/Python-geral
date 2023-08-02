# import math e use a funcao

from math import trunc

num = float(input('Digite um valor : '))

print('='*20)
print('O número {} tem a parte inteira {} '.format(num, trunc(num)))
print('='*20)