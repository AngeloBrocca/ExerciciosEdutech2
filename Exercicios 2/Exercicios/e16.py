#Escreva um programa que pergunte a quantidade de Km percorridos por 
# um carro alugado e a quantidade de dias pelos quais ele foi alugado.
#  Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e 
# R$0,15 por Km rodado.

km = int(input('Quantos km o carro alugado percorreu? '))
dias = int(input('Por quantos dias o carro foi alugado? '))

calculo_km = km * 0.15
calculo_dias = dias * 60
preco = calculo_km + calculo_dias

print(f"Preço total a pagar: R${preco.__round__(2)}")