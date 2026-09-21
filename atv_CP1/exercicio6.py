qtd_minutos = int(input('Digite a quantidade de minutos: '))

horas = qtd_minutos // 60

minutos_restantes  = qtd_minutos % 60

print(f'{horas} h 20{minutos_restantes} minutos')