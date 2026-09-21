valor_compra = float(input('Qual o valor da compra?: '))

membro = input('Você é membro do programa de fidelidade? S/N: ')

if valor_compra >= 200 or membro == 'S':
    print('Frete gratis')
else:
    print('Sem frete gratis')

