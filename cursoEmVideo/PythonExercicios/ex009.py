# tabuada

num = float(input('Digite o numero que quer a tabuada\n'))

for i in range(1, 11):
    print('{} * {} = {:.2f}'.format(num, i, (num * i)))
