#Elabore um programa que receba quatro notas de um aluno e calcule a média dessas notas.

import os

os.system('cls')

print('='*70)
print('Vamos calcular a média de quatro notas de alunos: ')
print('='*70)
print()

print('='*70)
n1 = float(input('Me diga a nota 1: '))
n2 = float(input('Me diga a nota 2: '))
n3 = float(input('Me diga a nota 3: '))
n4 = float(input('Me diga a nota 4: '))
print('='*70)
print()

media = (n1 + n2 + n3 + n4) / 4

print('='*70)
print('Média')
print('='*70)
print()

print(f'As notas {n1}, {n2}, {n3} e {n4}')
print(f'Possuem a média: {media}')
print()