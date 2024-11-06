#Faça um programa que receba o nome completo de uma pessoa e, em seguida, 
#mostre o primeiro e o último nome.

import os


os.system('cls')

nome = input('Me diga seu nome: ')
print()

lista = nome.split()

primeiro = lista[0:1]
ultimo = lista[-1:]

print(f'Seu priemiro e ultimo nome: {primeiro}, {ultimo}')
print()