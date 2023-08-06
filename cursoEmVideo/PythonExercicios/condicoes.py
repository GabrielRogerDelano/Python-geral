n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1 + n2)/2
print('Sua média foi: {}'.format(m))
if m >= 6.0:
    print('PARABÉNS! Uma ótima média!')
else:
    print('Sua média não foi muito boa! Estude mais na próxima.')
if m == 10.0:
    print('Uma média 10 é ótima! Continue assim! É será muito bem recompensado pelo seu esforço!')
