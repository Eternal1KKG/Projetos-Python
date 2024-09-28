# Questão 2: Condições Compostas
#    - Enunciado: Pergunte ao usuário dois valores: sua idade e se ele possui permissão dos pais (sim/não). Se o usuário tiver menos de 18 anos e não tiver permissão dos pais, ele não pode participar da viagem. Use operadores lógicos para avaliar as condições.
# Código Inicial:
idade = int(input("Digite sua idade: "))
permissao = input("Você tem permissão dos pais? (sim/não): ")
# Adicione sua estrutura de decisão aqui
if idade >= 18:
    if permissao == "sim":
        print("Você pode participar da viagem.")
else:
    print("Você não pode participar da viagem.")