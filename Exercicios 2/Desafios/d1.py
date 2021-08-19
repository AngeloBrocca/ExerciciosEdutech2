#Monte um sistema financeiro onde você tem que inserir o cadastro de novos
#funcionários, a cada 3 funcionários inseridos, o salário de todos eles 
#sobem 5% dovalor, de maneira incremental. Quando o sistema perceber que 
#você inseriu 10 funcionários, pausar o programa, e printar todos os 
#funcionários, e sortear um funcionário para que esse seja premiado e 
#receba o valor de 10% do seu salário de bônus

import random

funcionarios = []
salario = 1000

def cadastrador(nome):
    funcionarios.append(nome)

n = 1
s = 1

while n <= 10:
    cadastrador(input('Insira o nome do novo funcionário: '))
    n+=1
    s+=1

    if(s == 3):
        salario = salario * 1.05
        s = 0

if(len(funcionarios) == 10):
    print(f'Parabéns {random.choice(funcionarios)}! Você ganhou um bonus de 10% no salário!')
    print(f'Seu novo salário é de {round(salario * 1.1, 2)} reais')

print(f'Salário da equipe agora com {len(funcionarios)} funcionários: {round(salario, 2)} reais.')