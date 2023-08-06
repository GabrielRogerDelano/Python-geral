a = int(input("Primeiro valor : "))
b = int(input("Segundo valor : "))
c = int(input("Terceiro valor : "))

#menor
if a < b and a < c:
    menor = a
elif b < a and b < c:
    menor = b
else:
    menor = c

#maior
if a > b and a > c:
    maior = a
elif b > a and b > c:
    maior = b
else:
    maior = c

print('O maior é {}'.format(maior))
print('E menor é {}'.format(menor))