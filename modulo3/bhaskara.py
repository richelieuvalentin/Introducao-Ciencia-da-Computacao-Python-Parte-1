# Módulo MATH para funções Matemáticas
import math


# Recebe os valores de a, b e c

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

# Calcula o valor do discriminante

delta = b ** 2 -4 * a * c


# Para o caso do delta maior que zero

if delta > 0:
    raiz1 = (-b + math.sqrt(delta)) / (2 * a)
    raiz2 = (-b - math.sqrt(delta)) / (2 * a)

    if raiz1 > raiz2:
        print("as raízes da equação são", raiz2,"e",raiz1)

    else:
        print("as raízes da equação são", raiz1,"e",raiz2)
        
        
# Para o caso do delta igual a zero
elif delta == 0:
    raiz1 = (-b + math.sqrt(delta)) / (2 * a)
    print("a raiz desta equação é", raiz1)
    

# Para o caso do delta menor que zero
else:
    print("esta equação não possui raízes reais")
  




    

