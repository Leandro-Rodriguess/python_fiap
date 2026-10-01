mes = int(input('Digite o numero do mes (1 a 12): '))

match mes:
    case 1|2|3:
        print('1 trimestre')

    case 4|5|6:
        print('2 trimestre')

    case 7|8|9:
        print('3 trimestre')
    
    case 10|11|12:
        print("Quarto trimeste")

    case _:
        print('Mes invalido')