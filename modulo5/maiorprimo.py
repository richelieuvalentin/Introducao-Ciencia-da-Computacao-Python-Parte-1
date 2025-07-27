def e_primo(k):
   
    if k < 2:                      
        return False
    div = 2
    while div * div <= k:          
        if k % div == 0:           
            return False
        div += 1
    return True                    


def maior_primo(n):
   
    i = 2                          
    maior_primo = None             

    while i <= n:                  
        if e_primo(i):             
            maior_primo = i
        i += 1                     

    return maior_primo
