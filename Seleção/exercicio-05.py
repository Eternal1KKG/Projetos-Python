#Escreva um programa para ler um valor e escrever se é positivo ou negativo. Considere o valor zero como positivo.

#entradas
valor = int(input("Escreva um valor:"))

#processamento
resposta = ""
if valor >= 0:
   resposta = "positivo."
else:
   resposta = "negativo."

#saidas
print("O número é", resposta)