# receba um ângulo e diga o cosseno, seno e tangente

from math import cos, sin, tan, radians

ang = float(input('Digite um ângulo : '))

cos = cos(radians(ang))
sen = sin(radians(ang))
tan = tan(radians(ang))

print('='*20)
print('O ângulo {} tem: \ncosseno = {:.2f}\nseno = {:.2f}\ne tangente = {:.2f}'.format(ang, cos, sen, tan))
print('='*20)