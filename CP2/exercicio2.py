while True:
    print('1 - Somar')
    print('2 - Subtrair')
    print('3 - Multiplicar')
    print('4 - Dividir')
    print('5 - Sair')

    opcao = input('Opção: ')
 
    match opcao:
        case '1':

            numero1 = float(input('Primeiro número: '))
            
            numero2 = float(input('Segundo número: '))
            print('Resultado:', numero1 + numero2)
        case '2':

            numero1 = float(input('Primeiro número: '))

            numero2 = float(input('Segundo número: '))
            print('Resultado:', numero1 - numero2)

        case '3':
            numero1 = float(input('Primeiro número: '))

            numero2 = float(input('Segundo número: '))
            print('Resultado:', numero1 * numero2)
        case "4":
            numero1 = float(input('Primeiro número: '))

            numero2 = float(input('Segundo número: '))

            if numero2 == 0:
                print('Não é possível dividir por zero.')

            else:
                print('Resultado:', numero1 / numero2)

        case '5':
            print('Fim do programa')
            break

        case _:
            print('Opção invalida')
 