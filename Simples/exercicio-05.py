#Escreva um programa para ler as dimensões de uma cozinha retangular (comprimento, largura e
#altura), calcular e escrever a quantidade de caixas de azulejos para se colocar em todas as suas
#paredes (considere que não será descontada a área ocupada por portas e janelas). Cada caixa de
#azulejos possui 1,5 m2.

#entrada
comprimentoM = int(input("Em metros, qual é o comprimento da cozinha?"))
alturaM = int(input("Em metros, qual é a altura da cozinha? "))
larguraM = int(input("Em metros, qual a largura da cozinha?"))
caixaAzulejoM = 1.5

#processamento
pisoM = (comprimentoM * larguraM)
tetoM = pisoM
parede1 = (larguraM * alturaM)
parede2 = (comprimentoM * alturaM)
areaM = (pisoM + tetoM + parede1 * 2 + parede2 * 2)
caixaAzulejoQuant = (areaM / caixaAzulejoM)

#saida
print("Serão necessárias" , str(caixaAzulejoQuant) , "caixas.")