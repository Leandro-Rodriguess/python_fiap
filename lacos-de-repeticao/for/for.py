for numero in range(1, 6,1):
    print(numero)



""" exercicios """


""" # 1. 

# Dado o valor inicial e o final pelo usuário, exiba os números do intervalo FECHADO.

# ENTRADA: 4 9       SAÍDA: 4 5 6 7 8 9


inicio = int(input('Digite o valor inicial: '))
fim = int(input('Digite o valor final: '))

for i in range(inicio, fim + 1):
    print(i, end=' ')


# 2. 

# Dado o valor inicial e o final pelo usuário, exiba os números do intervalo ABERTO.

# ENTRADA: 4 9       SAÍDA: 5 6 7 8 

inicio = int(input('Digite o valor inicial: '))
fim = int(input("Digite o valor final: "))

for i in range(inicio + 1, fim):
    print(i, end=" ")


# 3.

# Dado um numero pelo usuário, exibir os seus 10 primeiros múltiplos.

# ENTRADA: 5        SAÍDA: 5 10 15 20 25 30 35 40 45 50

numero = int(input('Digite um número: '))

for i in range(1, 11):
    print(numero * i, end=" ")


# 4.

# Dado um numero pelo usuário e um multiplicador M, exibir os seus M primeiros múltiplos.

# ENTRADA: 5  6     SAÍDA: 5 10 15 20 25 30 


numero = int(input('Digite um número: '))
m = int(input('Digite o multiplicador M: '))

for i in range(1, m + 1):
    print(numero * i, end=" ") """