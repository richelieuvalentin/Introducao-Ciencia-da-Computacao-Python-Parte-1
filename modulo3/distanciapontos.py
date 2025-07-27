
# Módulo MATH para funções Matemáticas

import math

# Coordenadas do plano cartesiano

x_a = float(input("Digite a coordenada x do ponto a: "))
x_b = float(input("Digite a coordenada y do ponto a: "))

y_a = float(input("Digite a coordenada x do ponto b: "))
y_b = float(input("Digite a coordenada x do ponto a: "))

# Distância entre os pontos a e b

distancia_ab = math.sqrt((x_a - x_b) ** 2 + (y_a - y_b) ** 2)


if distancia_ab > 10:
            print("longe")

else:
    print("perto")

            
