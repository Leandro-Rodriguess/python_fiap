lado1 = float(input("Digite o primeiro lado: "))
lado2 = float(input("Digite o segundo lado: "))
lado3 = float(input("Digite o terceiro lado: "))

if (lado1 <= 0 or lado2 <= 0 or lado3 <= 0):
    print("Medidas inválidas")

elif (lado1 + lado2 <= lado3 or lado1 + lado3 <= lado2 or lado2 + lado3 <= lado1):
    print("Não forma um triajngulo")

elif lado1 == lado2 == lado3:
    print("Triângulo equilátero")

elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("Triangulo isosceles")

else:
    print("Triangulo escaleno")