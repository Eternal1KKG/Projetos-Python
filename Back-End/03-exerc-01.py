#  Questão 1: Classificação por Faixa Etária
#    - Enunciado: Peça a idade do usuário e classifique-o em categorias ('Criança', 'Adolescente', 'Adulto', 'Idoso') usando "if-elif-else".
# Código Inicial:
idade = int(input("Digite sua idade: "))
mensagem =("Você é parte da categoria:")
# Adicione sua estrutura de decisão aqu

if idade <= 59:
    if idade <= 13:
        print(mensagem, "Criança")
    elif idade <= 19:
        print(mensagem, "Adolescente")

    elif idade <= 59:
        print(mensagem, "Adulto")
else:
    print(mensagem, "Idoso")
