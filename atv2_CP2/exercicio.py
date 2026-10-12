inicio = int(input("Digite o primeiro número: "))
fim = int(input("Digite o segundo número: "))

for numero in range(inicio, fim + 1):
    print(numero)


if inicio < fim:
    for numero in range(inicio, fim + 1):
        print(numero)

if inicio > fim:
    for numero in range(inicio, fim - 1 , -1):
        print(numero)