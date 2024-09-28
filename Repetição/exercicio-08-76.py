# Construa um algoritmo que leia 50 valores inteiros e positivos e:
# · Encontre o maior valor
# · Encontre o menor valor
# · Calcule a média dos números lidos

#OBS1. Refaça o exercício usando lista para armazenarmos valores digitados pelo usuário.
#OBS2. Faça com que o sistema sorteie 6 valores digitados pelo usuário logo após exiibir as mensagens.

#entrada
import random
maior = 0
menor = 9999999
soma = 0
limiteValor = 10
limiteSorteio = 5
listValores = []
listPar = []
listImpar = []

#processamento
for itemValor in range(1, limiteValor + 1):
    # valor = int(input(f"Qual o {itemValor}º valor? "))
    valor = random.randrange(1, 101)
    if(valor > maior):
        maior = valor

    if(valor < menor):
        menor = valor
    soma = soma + valor
    # print("soma: ", soma)
    listValores.append(valor)



for itemValor in listValores:
    if(itemValor % 2 == 0):
        listPar.append(itemValor)
        #print("Par: ", itemValor)

for itemValor in listValores:
    if(itemValor % 2 != 0):
        listImpar.append(itemValor)
        # print("Impar: ", itemValor)

#saida
media = (soma / limiteValor)
print("Valores: ", listValores)
print("Valores pares: ", listPar)
print("Valores impares: ", listImpar)
print("Maior valor: ", maior)
print("Menor valor: ", menor)
print("Média dos valores: ", media)

listSorteados =  []
for itemindex in range(limiteSorteio + 1):
    index = random.randrange(0,  10)
    listSorteados.append(listValores[index])
print("Números sorteados:", listSorteados)