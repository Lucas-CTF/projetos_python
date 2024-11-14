#Faça um programa que imprima os números pares entre 0 e 100.

import os


os.system('cls')

print('='*70)
print('Numeros pares de 0 a 100')
print('='*70)

contador = 0

for var_iteradora in range (0, 101):
    if var_iteradora % 2 != 0:
        continue

    else:
        print(var_iteradora, end=' ')
        