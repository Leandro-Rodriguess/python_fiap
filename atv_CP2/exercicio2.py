cor = input('Dgite a cor do semaforo: ').strip().lower()

match cor:
    case 'vermelho':
        print('Pare')

    case 'amarelo':
        print('Atenção')

    case 'verde':
        print('Siga')

    case _:
        print('Cor invalida ')