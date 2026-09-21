numero = int(input('Digite um numero inteiro: '))

if numero < 1 or numero > 100:
    print(f'{numero} está fora do intervalo de 1 a 100')

else:
    print(f'{numero} está dentro do intervalo de 1 a 100')