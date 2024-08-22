# Escreva um programa para ler 2 valores (considere que não serão informados valores iguais) e
# escrever o maior deles.

#entrada
valor1 = float(input("Digite um primeiro valor: ").replace(',','.'))
valor2 = float(input("Digite um segundo valor: ").replace(',','.'))
#processamento
resultado = ""
if valor1 > valor2:
    resultado = valor1
else:
    resultado = valor2

#saida
print("O valor", resultado,  "é maior.")        