valorInicial = int(input("Qual seria o valor inicial? "))
valorFinal = int(input("Qual seria o valor final? "))
multiplo = int(input("Qual seria o múltiplo? "))

if(valorFinal < valorFinal):
    for i in range(valorInicial, valorFinal + 1):
        if(i % multiplo == 0):
            print(i, "multiplo ", multiplo)
        
        else:
            print(i)

else:
    print("DADOS INVÁLIDOS!")            
    
       
 