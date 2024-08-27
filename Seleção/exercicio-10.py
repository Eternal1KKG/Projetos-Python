# 10) Escreva um programa para ler 3 valores inteiros (considere que não serão lidos valores iguais) e escrevê-los em ordem crescente.

# entrada
valores = []
valores.append(int(input("Digite o primeiro valor?")))
valores.append(int(input("Digite o segundo valor?")))
valores.append(int(input("Digite o terceiro valor?")))

#processamento
if (valores[0] > valores[1]):
    valorTemp = valores[0]
    valores[0] = valores[1]
    valores[1] = valorTemp

if (valores[0] > valores[2]):
    valorTemp = valores[0]
    valores[0] = valores[2]
    valores[2] = valorTemp

if (valores[1] > valores[2]):
    valorTemp = valores[1]
    valores[1] = valores[2]
    valores[2] = valorTemp  

for x in valores:
    print(x) #saida
