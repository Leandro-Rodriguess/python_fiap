# Exercício 4

# Faça um programa em Python que solicite ao usuário:

# o valor recebido por hora trabalhada;

# a quantidade de horas trabalhadas no mês.

# Em seguida, o programa deve calcular o salário total mensal, multiplicando o valor da hora pela quantidade de horas trabalhadas.

# Ao final, exiba na tela o salário total do trabalhador.


valor_hora = float(input('Digite o valor da sua hora trabalhada'))
qtd_horas = int(input('Digite a quantidade de horas trabalhadas no mês: '))

salario_total = valor_hora * qtd_horas

print(f'O seu slsario é de {salario_total}')