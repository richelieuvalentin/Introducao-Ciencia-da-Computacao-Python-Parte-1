
print("Digite uma sequência terminada por um.")

produto = 1
valor = 0

while valor != 1:
    valor = int(input("Digite um valor a ser multiplicado: "))
    produto = produto * valor

print("O produto dos valores digitados é", produto)
