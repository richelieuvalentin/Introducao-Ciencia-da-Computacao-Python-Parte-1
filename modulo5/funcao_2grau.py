# Função para calcular as raízes de equação do 2º grau

import math

def discriminante(a, b, c):
    """Calcula o valor de delta"""
    return b ** 2 -4 * a * c
    


def raizes(a, b, c):
    """Calcula as raizes da equação"""

    delta = discriminante(a, b, c)

    if delta < 0:
       print("A equação não possui raizes reais!")

       return None


    elif delta == 0:
        x = -b / (2*a)

        return x
    

    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)

        return x1, x2


        
    
    

    
  


