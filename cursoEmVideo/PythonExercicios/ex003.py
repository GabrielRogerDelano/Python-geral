n1 = int(input('Digite um valor = '))
n2 = int(input('Digite outro valor = '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma vale {}, a multiplicacao vale {} e a divisao da {:.3f}'. format(s, m, d), end=' ')
print('A divisao inteira é {} e a potencia é {}'.format(di, e))
