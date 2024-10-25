#Implemente um programa que receba dois números e realize a divisão, formatando o resultado com quatro casas decimais.
#Para imprimir um resultado com quatro casas decimais usamos a função ":.(numero de casas)f" tipo "":.4f"

import os

os.system('cls')

print('Divisão')
print()

n1 = float(input('Me diga o numero que sera dividido: '))
n2 = float(input('Me diga o divisor dele: '))
print()

d = n1 / n2

print(f'Sua divisão deu : {d:.4f}')
print()