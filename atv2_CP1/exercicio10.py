idade = int(input('Digite sua idade: '))

altorizacao = input('Você tem altorização S/N: ')

if idade >= 18 or altorizacao == 'S':
    print('Acesso permitido')

else:
    print('Acesso negado')