#Escreva um programa para ler o raio de um círculo, calcular e escrever a sua área
#(pi * (raio * raio))

#entrada
raio = int(input("Qual o raio?"))
pi = 3.14 #constante

#processamento
area = (pi * (raio * raio))

#saida
print("A área do circulo é" , str(area))