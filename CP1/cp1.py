salario = float(input('Digite o salario : '))
faltas = int(input('Digite a quantidade de faltas: '))



if salario < 0 and faltas < 0:
    print('ERRO! Digite um salario positivo')
    

else:
    salario_minimo = 1302
   
    if salario <=  2 * salario_minimo:
        percentual = 0.0645

    elif salario <= 5 * salario_minimo:
        percentual = 0.455

    else:
        percentual = 0.0289


    salario_reajustado = salario + (salario * percentual)


    if faltas == 0:
        bonus = 1302
        salario_reajustado += salario_minimo
        print('você recenberá um bonus de salario minimo')

    elif faltas == 1:
        bonus = 500
        salario_reajustado += 500
        print('Seu bonus foi de 500 reais ')

    else:
        bonus = 0
        salario_reajustado += 0
        print('você não recebera bonus')


    salario_total = salario_reajustado


    print('----------------- Final ----------------------------\n')

    print('--------------- Salário -------------')
    print(f'Seu salario foi de {salario}')
    print('-------------------------------------\n')
    print('---------- Salário Reajustado --------- ')
    print(f'seu salario reajustado foi de {salario_reajustado}')
    print('--------------------------------------\n')

    print('------------------------------------')
    print(f'Seu bonus foi de {bonus}')
    print('---------------------------------\n')

    print(f'---------------- Ganho total --------------')
    print(f'Seu ganho total foi de {salario_total:.2f}\n')