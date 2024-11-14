#Faça um programa que imprima os números no intervalo entre 1 e 10 em ordem inversa.

import os


os.system('cls')

print('='*70)
print('Numeros de 10 a 1')
print('='*70)

for var_iteradora in range (10, 0, -1):
    print(var_iteradora, end=' ')