#Escreva um programa para ler uma temperatura em graus Fahrenheit, calcular e escrever o valor
#correspondente em graus Celsius (C = (F-32) * 5 / 9)

#entrada
grausF = int(input("Em Fahrenheit, Digite quantos graus."))

#processamento
grausC = (grausF - 32) * 5/9

#saida
print("Graus em Celsius =" , str(grausC))