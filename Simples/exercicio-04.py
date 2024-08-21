#) Escreva um programa para calcular e imprimir o número de lâmpadas necessárias para iluminar um
#determinado cômodo de uma residência. Dados de entrada: a potência da lâmpada utilizada (em watts),
#as dimensões (largura e comprimento, em metros) do cômodo. Considere que a potência necessária é
#de 18 watts por metro quadrado

#entrada
potenciaLampadaWatts = int(input("Em Watts, qual a potência da lâmpada?"))
largura = int(input("Em metros, qual é a largura do cômodo?"))
comprimento = int(input("Em metros, qual é o comprimento do cômodo?"))

#processamento
area = (largura * comprimento)
capacidadeIluminacao = (potenciaLampadaWatts / 18)
quantidadeLampada = (area / capacidadeIluminacao)

#saida
print("A quantidade de lâmpadas necessárias é" , str(quantidadeLampada))