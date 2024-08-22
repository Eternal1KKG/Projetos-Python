# As maçãs custam R$ 0,30 cada se forem compradas menos do que uma dúzia, e R$ 0,25 se forem
# compradas pelo menos doze. Escreva um programa que leia o número de maçãs compradas, calcule e
# escreva o valor total da compra.

#entrada
maca = 0.30
macaporduzia = 0.25
macascomprada = int(input("Quantas maçãs você comprou? "))

#processamento
valortotal = ""
if macascomprada >= 12:
    valortotal = macaporduzia * macascomprada
else:
    valortotal = maca * macascomprada

#saida
print("O valor total de sua compra foi: R$", valortotal)