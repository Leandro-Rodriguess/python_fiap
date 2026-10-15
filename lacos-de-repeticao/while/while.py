""" contador = 1

while contador <= 5:
    print(contador)
    contador += 1

 """
import os
os.system("cls")
 
# Laço condicional while - usado para quantidade de repetições quando não se sabe o número exato de iterações
 
# Exemplo: somar número até que seja digitado zero
 
# ENTRADA 4 5 1 7 3 4 1 0       SAÍDA: 15
 
soma = 0
num = 1

while num != 0:
    num = float(input("Número: "))
    soma = soma + num

print(f"Soma: {soma}")