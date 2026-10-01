valor = float(input("Digite o valor da compra: R$ "))

if valor < 0:
    print("Valor invalido")
elif valor < 100:
    final = valor
elif valor < 300:
    final = valor * 0.95
elif valor < 500:
    final = valor * 0.90
else:
    final = valor * 0.85

if valor >= 0:
    print(f"Valor final: R$ {final:.2f}")