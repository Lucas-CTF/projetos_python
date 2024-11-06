#Faça um programa que receba o nome completo de uma pessoa e, posteriormente, 
# imprima esse nome separadamente.

import os


os.system('cls')

nome = input("Me diga seu nome: ")
print()

#aqui o split funciona assim:
# se voce colocar "separado = nome.split("a") e dpois 
# digitar: "Lucao Danielo Bolo"
# a saida sera: "Seu nome separado: ['Luc', 'o D', 'nielo Bolo']"
# porque o split pega o caracter que voce colocar no parenteses, exclui 
# ele da frase e separa a partir dele
#melhor é deixar um espaço vazio mesmo como esta
separado = nome.split()

print(f'Seu nome separado: {separado}')
print()