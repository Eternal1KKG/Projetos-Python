# Escreva um programa para ler o ano de nascimento de uma pessoa e escrever uma mensagem que
#diga se ela poderá ou não votar este ano (não é necessário considerar o mês em que ela nasceu).
#e

from datetime import date

#entrada
#anoAtual = date.today().year
anoNascimento = int(input("Qual ano você nasceu? "))

#processamento
def verificarOpcao():
    #idade = anoAtual - anoNascimento
    if (idade(anoNascimento) > 16):
        return "Sim"
    else:
        return "Não"
def idade(nascimento):
    anoAtual = date.today().year
    return anoAtual - anoNascimento

#saida  
print("Você poderá votar?:", verificarOpcao())  
print("Porque você tem", idade(anoNascimento), "anos.")