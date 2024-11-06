#Faça um programa que solicite separadamente o nome, o nome do meio e o sobrenome de uma pessoa. Em seguida, imprima o nome completo.

import os


os.system('cls')

nome = input('Me diga seu nome: ')
nome_do_meio = input('O do meio: ')
sobrenome = input('Sobrenome: ')
print()

print(f'Seu nome é {nome} {nome_do_meio} {sobrenome}')
print()