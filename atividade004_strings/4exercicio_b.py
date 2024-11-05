#Faça um programa que receba o nome 'João da Silva' e, em seguida, substitua 'Silva' por 'Oliveira'.

import os


os.system('cls')

original = 'João da Silva'
novo = original.replace("Silva", "Oliveira")

print(f'Nome original: {original} \nNome novo: {novo}')