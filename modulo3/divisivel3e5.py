numero = int(input("Digite o número a ser verificado: "))

if numero % 3 == 0 and numero % 5 == 0:
    print("FizzBuzz")
else:
    print(numero)
