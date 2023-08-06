# leia de 0 a 9999 e diga: qual representa a unidade, dezena, centena e milhar

numero = int(input("Digite um numero entre 0 e 9999 : \n"))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10

print("Unidades : ", u)
print("dezenas : ", d)
print("centenas : ", c)
print("milhares : ", m)

'''numero = int(input("Digite um numero entre 0 e 9999 : \n"))
num = str(numero)
print('O numero {} tem : \n'.format(num))


print("Unidades : " + num[-1])
print("dezenas : " + num[-2])
print("centenas : " + num[-3])
print("milhares : " + num[-4])
'''


