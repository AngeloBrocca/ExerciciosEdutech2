# Faça um programa que insira um valor em reais, e 
# faça ele converter o valor para dólar, mostrando quantos
# dólares podem ser comprados com aquela quantia. 
# (Valor para ser usado do dólar no exercício: 5.30)

real = float(input('Insira valor em reais: '))
dolar = 5.30

cambio = real / dolar

print("Com R${0} você pode comprar {1} dólares.".format(real, cambio.__round__(2)))