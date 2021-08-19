#Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
#Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo 
# na tela o nome do escolhido.

import random

aluno1 = input('insira o nome do aluno 1(a): ')
aluno2 = input('insira o nome do aluno(a) 2: ')
aluno3 = input('insira o nome do aluno(a) 3: ')
aluno4 = input('insira o nome do aluno(a) 4: ')

lista = [aluno1, aluno2, aluno3, aluno4]

print(f'O(A) aluno(a) escolhido(a) foi..... {random.choice(lista)}!!!!')