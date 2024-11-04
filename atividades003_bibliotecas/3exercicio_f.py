#Faça um programa onde o usuário tenta adivinhar o número que o computador está ‘pensando’.
import os
import random


os.system('cls')

print('='*70)
print('TENTE SABER O NUMERO QUE EU PENSEI ENTRE 1 E 20')
print('='*70)
print()

numero_sorteado = random.randint(1, 20)

