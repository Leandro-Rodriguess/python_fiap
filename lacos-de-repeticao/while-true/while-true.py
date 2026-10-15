""" while True:
    senha = input('Digite a senha: ')

    if senha == '1234':
        print("Acesso permitido!")
        break

    print('Senha incorreta. Tente novamente.') """

#Calcular a média de duas notas do usuário, enquanto for digitado s no continuar.
 
 
import os
os.system("cls")
 
opcao = "s"
 
while True:
 
    nota1 = float(input("Nota 1: "))
    if nota1 < 0 or nota1 > 10:
        print("Nota inválida")
        continue
 
    nota2 = float(input("Nota 2: "))
    if nota2 < 0 or nota2 > 10:
        print("Nota inválida")
        continue
 
    media = (nota1 + nota2) / 2
    print(f"As médias das notas: {nota1} e {nota2} é: {media:.2f}")
 
    opcao = input("Continuar? [S]im ou [N]ão:  ")
   
    opcao.upper()
 
    while opcao.upper() not in ['S', 'N']:
        opcao = input("ERRO! Digite S ou N: ")
    else:
        if opcao == 'n' or opcao == 'N':
            break

