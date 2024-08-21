#A equipe Benneton-Ford deseja calcular o número mínimo de litros que deverá colocar no tanque de
#seu carro para que ele possa percorrer um determinado número de voltas até o primeiro
#reabastecimento. Escreva um programa que leia o comprimento da pista (em metros), o número total de
#voltas a serem percorridas no grande prêmio, o número de abastecimentos desejados e o consumo de
#combustível do carro (em Km/L). Calcular e escrever o número mínimo de litros necessários para
#percorrer até o primeiro reabastecimento. OBS: Considere que o número de voltas entre os
#abastecimentos é o mesmo.'''

#entrada
comprimento = int(input("Qual o comprimento da pista(em metros) ?"))
litrosAbastecidosNaCorrida = int(input("Quantos litros foram abastecidos ao carro durante a corrida ?"))
voltas = int(input("Quantas voltas o carro percorreu durante a corrida ?"))
reabastecimentosDesejados = int(input("Qual o minímo de reabastecimentos que você deseja no seu carro ?"))
consumoDoCarro = int(input("Quantos litros de combustível o carro consumiu durante a corrida ?"))

#processamento
kmTotal = (comprimento / 1000) * voltas
consumoTotal = kmTotal / consumoDoCarro
litros = consumoTotal / reabastecimentosDesejados

#saida
print("O número de litros necessários para chegar até o primeiro reabastecimento é" , str(litros))
