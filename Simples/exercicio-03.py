#Escreva um programa para ler uma temperatura em graus Celsius, calcular e escrever o valor
#correspondente em graus Fahrenheit. (F = (C × 9/5) + 32)

#entrada
grausC = int(input("Em Celsius, Digite quantos graus."))

#processamento
grausF = (grausC * 9/5) + 32

#saida
print("Graus em Fahrenheit =" , str(grausF))