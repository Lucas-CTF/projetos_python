#Implemente um programa que receba um número inteiro e imprima sua tabuada de multiplicação.

import os

os.system('cls')

n = int(input('Me diga o numero do qual você quer saber a tabuada: '))
print()

n2 = n *2
n3 = n *3
n4 = n*4
n5 = n*5
n6 = n*6
n7 = n*7
n8 = n*8
n9 = n*9
n10 = n*10

print(f'Tabuado do numero {n}:')
print(f'   {n} x 1 = {n}')
print(f'   {n} x 2 = {n2}')
print(f'   {n} x 3 = {n3}')
print(f'   {n} x 4 = {n4}')
print(f'   {n} x 5 = {n5}')
print(f'   {n} x 6 = {n6}')
print(f'   {n} x 7 = {n7}')
print(f'   {n} x 8 = {n8}')
print(f'   {n} x 9 = {n9}')
print(f'   {n} x 10 = {n10}')
print()