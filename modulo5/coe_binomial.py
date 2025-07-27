
# Função para calcular o Fatorial

def fatorial (n):

    fatorial = 1
    
    while n > 0:
        
        fatorial = fatorial * n
        n = n - 1
        
    return fatorial

# Função para calcular o coeficiente binomial

def binomial(n, k):
    return fatorial(n) / (fatorial(k) * fatorial(n-k))

# Teste

def testa_fatorial():
    if fatorial(1) == 1:
        print("Funciona para 1")
    else:
        print("Não funciona para 1")

    if fatorial(2) == 2:
        print("Funciona para 2")
    else:
        print("Não funciona para 2")

    if fatorial(0) == 1:
        print("Funciona para 0")
    else:
        print("Não funciona para 0")

    if fatorial(5) == 120:
        print("Funciona para 5")
    else:
        print("Não funciona para 5")

        
        

        
    
        
    
    
        


    
