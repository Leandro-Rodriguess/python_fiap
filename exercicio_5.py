# Exercício — Cálculo do valor da compra com desconto
# Faça um programa em Python que solicite ao usuário as seguintes informações:

# o nome de um produto;

# o preço unitário do produto;

# a quantidade de produtos comprados;

# o percentual de desconto que será aplicado sobre a compra.

# Depois, o programa deverá:

# Calcular o valor bruto da compra, multiplicando o preço do produto pela quantidade comprada.

# Calcular o valor do desconto com base no percentual informado.

# Calcular o valor final da compra, subtraindo o desconto do valor bruto.

# Exibir na tela o nome do produto, seu preço, a quantidade comprada e o valor final da compra.



nome_produto = input('Digite o nome do produto: ')
preco = float(input('Digite o preço do seu produto: '))
qtd_prodto = int(input('Quantos você comprou?: '))
desconto = int(input('Quanto de desconto?:'))

valor_bruto = preco * qtd_prodto

desconto_final = valor_bruto * (desconto / 100) # em porcentagem 

resultado_final = valor_bruto - desconto_final

print('-----------------------------------------------')
print(f'O nome do seu produto é {nome_produto}')

print('---------------------------------------------')
print(f'O preço dele é {preco}')

print('-------------------------------------------')
print(f'Você comprou {qtd_prodto} desse produto')

print('---------------- Valor Final --------------')

print(f'O valor final é {resultado_final}')