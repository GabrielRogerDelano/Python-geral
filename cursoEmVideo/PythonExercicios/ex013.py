# calcula aumento de salário

salario = float(input('Digite seu salário\n'))

# considerando 15% de aumento
aumento = 15/100

novoSalario = salario * (1 + aumento)

print('='*20)
print('Seu salário de R${} recebeu um aumento de {}% e passará a ser R${}'
      .format(salario, aumento * 100, novoSalario))
print('='*20)
