#Faça um programa que imprima os números no intervalo entre 1 e 100. Os números devem ser apresentados na horizontal.

import os


os.system('cls')

print('='*70)
print('Numeros de 1 a 100')
print('='*70)

for var_iteradora in range (1, 101):
    print(var_iteradora, end=' ')