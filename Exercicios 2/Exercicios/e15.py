#Escreva um programa que converta uma temperatura digitando em 
# graus Celsius e converta para graus Fahrenheit.

c = int(input('Insira temperatura em Celcius: '))

f = ((9*c)/5)+32

print('Temperatura(em °C e °F):\n - {0}°C\n - {1}°F'.format(c, round(f)))