numero = int(input("Digite um número a ser testado: "))

digito_adj_igual = False


while numero != 0 and not digito_adj_igual:
    digito = numero % 10
    numero = numero // 10
    digito_1 = numero % 10
    
    if digito == digito_1:
        digito_adj_igual = True

if digito_adj_igual:
    print("sim")

else:
    print("não")
    
    
