
numero = int(input("Digite o número para contarmos seus digítos: "))
soma = 0
digito = 0

while numero > 0:
    digito = numero % 10
    numero = numero // 10
    soma = soma + digito

print(soma)
             
             
             
