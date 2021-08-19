#Faça um programa que leia a largura e a altura de uma parede em metros,
#  calcule a sua área e a quantidade 
#de tinta necessária para pintá-la, sabendo que cada 
# litro de tinta pinta uma área de 2 metros quadrados.

largura = float(input("Insira a largura da parede (em metros): "))
altura = float(input("Insira a altura da parede (em metros): "))

area = largura * altura

tinta = area / 2

print("Para pintar {0}m² de parede são necessarios {1} litros de tinta.".format(area, tinta))