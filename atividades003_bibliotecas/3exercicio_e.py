#Faça um programa para sortear um número de 1 a 20.
#vamos trabalhar com a biblioteca random

import os
import random

os.system('cls')

print('='*70)
print('Numeros aleatorios')
print('='*70)
print()

#função para pegar numero aleatorio
numero = random.randint(1, 20)
print(f'Seu numero é : {numero}')
print()