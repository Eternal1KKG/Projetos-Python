#Escreva um programa para ler as notas das duas avaliações de um aluno no semestre, calcular e
# escrever a média semestral e a seguinte mensagem: PARABÉNS! Você foi aprovado! somente se o
# aluno foi aprovado (considere 6.0 a média mínima para aprovação).


#entrada
avaliacao1 = float(input("Digite a nota que você recebeu na primeira avaliação deste semestre:"))
avaliacao2 = float(input("Digite a nota que você recebeu na segunda avaliação deste semestre:"))

#processamento
mediasem = (avaliacao1 + avaliacao2) / 2
mensagem = ""
if mediasem >= 6:
    mensagem = "PARABÉNS! Você foi aprovado!"
else:
    mensagem = "Sentimos muito. Você foi reprovado."  

print("Sua média neste semestre foi:", mediasem, mensagem)