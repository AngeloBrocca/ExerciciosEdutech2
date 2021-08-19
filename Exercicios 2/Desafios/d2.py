#Realize um sistema que gere boletos, neste sistema, você irá inserir 
# o número do banco que será de exemplo: 341-7, o número de um boleto 
# que será um número aleatório entre 1000 e 10000, e incorpore dentro 
# desta linha também, mês, dia, e ano, acrescentar 8 vezes o número
#  0 e no final acrescentar o valor do boleto.

#O boleto deverá ficar assim:
#341-7 | 5004020820210000000039990

import random

numero_banco = input('Insira o número do banco:')
data = input('Insira a data do boleto (ddmmaa):')
valor = input('Insira o valor do boleto:')
numero_aleatorio = random.randint(1000, 10000)
zeros = '00000000'

print(f' Boleto: \n \n {numero_banco} | {numero_aleatorio}{data}{zeros}{valor}')