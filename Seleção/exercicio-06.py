#

#entradas
valor =int(input("Escreva um valor: "))

#processamento
resposta= ""
if valor == 0:
    resposta = "zero"
elif valor > 0:
    resposta = "positivo"
else:
    resposta = "negativo" 

#saidas
print("O seu valor é", resposta)