# verifique se forma um triangulo

a = float(input("Primeiro segmento : "))
b = float(input("Segundo segmento : "))
c = float(input("Terceiro segmento : "))

if a + b >= c and a + c >= b and b + c >= a:
    print('\033[1;32mPodem formar um triangulo')
else:
    print("\033[1;31mNao podem formar um triangulo")