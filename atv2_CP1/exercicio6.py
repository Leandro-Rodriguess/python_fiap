idade = int(input('Digite sua idade: '))

if idade < 12 or idade >= 60:
    print(f'Tem direito a desconto')

else:
    print('Não tem direito a desconto')