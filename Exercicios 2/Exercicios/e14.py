#Faça um algoritmo que leia o salário de um funcionário e mostre seu 
#novo salário, com 15% de aumento.

salario = float(input('Insira o salário do funcionário: '))
aumento = round(salario * 1.15, 2)

print('\n Salário antigo: {0} reais \n Novo salário: {1} reais\n'.format(round(salario), aumento))