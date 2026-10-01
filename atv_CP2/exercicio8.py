idade = int(input("Digite a idade: "))

if idade < 0:
    print("Idade invalida")
elif idade <= 5:
    print("Não paga")
elif idade <= 12:
    print("R$ 10,00")
elif idade <= 59:
    print("R$ 25,00")
else:
    print("R$ 12,00")