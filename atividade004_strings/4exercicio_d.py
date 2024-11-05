#Faça um programa que leia uma frase e depois exiba na tela: 
# A frase em minúsculas, a frase em maiúsculas, a quantidade de caracteres na frase 
# e quantas letras tem a 2ª palavra na frase.

import os


os.system('cls')

frase = 'Pequeno Conjunto de Letras'
print(f'Frase: {frase}')

quantidade_de_caracteres = len(frase)
minusculas = frase.lower()
maiuscula = frase.upper()
segunda_palavra = len("conjunto")

print(f'Quantidade de letras na frase: {quantidade_de_caracteres}\n\
Tudo minusculo: {minusculas}\nTudo maiusculo: {maiuscula}\n\
Quantidade de caracteres na segunda palavra: {segunda_palavra}')
print()