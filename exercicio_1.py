# Questão 1

# Faça um programa em Python que solicite ao usuário a digitação de um número inteiro. Em seguida, o programa deverá mostrar na tela:

# O número digitado;

# O seu antecessor (número anterior);

# O seu sucessor (número posterior).



numero = int(input('Digie o seu numero: '))

print(f'Seu numero é {numero}')
print(f'O antecessor é', numero -1 )
print(f'O sucessor é', numero + 1)


