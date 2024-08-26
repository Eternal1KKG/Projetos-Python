# Escreva um programa que leia as notas das duas avaliações normais e a nota da avaliação optativa.
# Caso o aluno não tenha feito a optativa deve ser fornecido o valor -1. Calcular a média do semestre
# considerando que a prova optativa substitui a nota mais baixa entre as duas primeiras avaliações.
# Escrever a média e mensagens que indiquem se o aluno foi aprovado, reprovado ou está em exame, de
# acordo com as informações abaixo:
# Aprovado : média >= 6.0 Reprovado: media < 3.0 Exame: média >= 3.0 e < 6.0


#entrada
avaliacao1 = float(input("Digite a nota que você recebeu na primeira avaliação: ").replace(',','.'))
avaliacao2 = float(input("Digite a nota que você recebeu na segunda avaliação: ").replace(',','.'))
verificarOptativa = input("Você fez o teste optativo ? ")

#processamento
if  verificarOptativa == "sim":
    optativaNota = float(input("Digite a nota que você recebeu na avaliação optativa: ").replace(',','.'))
    
else:
    optativaNota = -1
    media = (avaliacao1 + avaliacao2 + optativaNota) / 2    
    print("Sua média do semestre foi: ", media)
    exit()

if avaliacao1 > avaliacao2:
    avaliacao2 = optativaNota
    media = (avaliacao1 + optativaNota) / 2
    print("Sua média do semestre foi: ", media)
else: 
    avaliacao1 = optativaNota
    media = (avaliacao2 + optativaNota) / 2
    print("Sua média do semestre foi: ", media)