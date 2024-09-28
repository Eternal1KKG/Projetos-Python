# Questão 2: Avaliação Escolar
#    - Enunciado: Escreva um programa que peça a nota final de um aluno e o classifique em 'Excelente', 'Bom', 'Satisfatório', 'Insuficiente', usando uma estrutura de decisão encadeada.
# Código Inicial:
nota = float(input("Digite a nota do aluno: "))
mensagem =("Seu resultado foi:")
# Adicione sua estrutura de decisão aqui

if nota <= 9:
    if nota <= 5:
        print(mensagem, "Insuficiente")
    elif nota <= 7:
        print(mensagem, "Satisfatório")
    elif nota <= 9:
        print(mensagem, "Bom")
if nota == 10:
    print(mensagem, "Excelente")
