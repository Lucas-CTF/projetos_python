#Desenvolva um programa que peça um número qualquer e calcule o dobro e o triplo desse número.

import os

os.system('cls')

n = float(input('Me diga o numero que deseja saber o dobro e o triplo: '))
print()

d = n * 2
t = n * 3

print(f'O dobro de {n} é {d} e o triplo é {t}.')