
def ehprimo(n):

    if n < 2:
        return False

    divisor = 2
    maiorprimo = 0
    
    while divisor <= n:
        if n % divisor == 0:
            maiorprimo = divisor

        divisor = divisor + 1
        return maiorprimo
            
            
        
