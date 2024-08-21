#Um motorista de táxi deseja calcular o rendimento de seu carro na praça. Sabendo-se que o preço do
#combustível é de R$ 4,87, escreva um programa para ler: a marcação do odômetro (Km) no início do
#dia, a marcação (Km) no final do dia, o número de litros de combustível gasto e o valor total (R$)
#recebido dos passageiros. Calcular e escrever: a média do consumo em Km/L e o lucro (líquido) do dia.

#entrada
combustivelLitroPreco = int(input("Em reais, qual o preço do combustível por litro?"))
combustivelLitroGasto = int(input("Quantos litros foram gastos?"))
kmComecoDia = int(input("Quantos Kms estavam marcados no começo do dia?"))
kmFimDia = int(input("Quantos Kms estavam marcados no FIM do dia?"))
valorRecebido = int(input("Qual foi o valor total recebido no fim do dia?"))

#processamento
kmPercorrido = (kmFimDia - kmComecoDia)
consumoKmLitro = (kmPercorrido / combustivelLitroGasto)
combustivelGastoPreco = (combustivelLitroGasto * combustivelLitroPreco)
lucro = (valorRecebido - combustivelGastoPreco)

#saida
print("Você consumiu em média" , str(consumoKmLitro) , "litros por Km")
print("Você teve" , str(lucro) , "reais de lucro hoje!")