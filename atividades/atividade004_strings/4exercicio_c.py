#Faça um programa que leia o nome de uma pessoa e verifique se a palavra 'Oliveira' está presente neste nome, mostrando True ou False.

import os


os.system('cls')

nome = input('Me diga seu nome: ')
print()

if "Oliveira" in nome:
    print('Seu nome tem "Oliveira"')
else:
    print('Seu nome não tem "Oliveira"')