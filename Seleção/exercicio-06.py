#

#entradas
valor =  float(input("Escreva um valor: ").replace(',','.'))

#processamento
resposta= ""
if valor == 0:
    resposta = "zero."
elif valor > 0:
    resposta = "positivo."
else:
    resposta = "negativo." 

#saidas
print("O seu valor é", resposta)