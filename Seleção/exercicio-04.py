# Acrescente ao exercício anterior a mensagem Você foi REPROVADO! Estude mais... caso a
# média calculada seja menor que 6.0.

#entrada
avaliacao1 = float(input("Digite a nota que você recebeu na primeira avaliação deste semestre: ").replace(',','.'))
avaliacao2 = float(input("Digite a nota que você recebeu na segunda avaliação deste semestre: ").replace(',','.'))

#processamento
mensagem = ""
mediasem = (avaliacao1 + avaliacao2) / 2
if mediasem >= 6:
    mensagem = "PARABÉNS! Você foi aprovado!"
else:
    mensagem = "Você foi REPROVADO! Estude mais...."  

print("Sua média neste semestre foi:", mediasem, mensagem)