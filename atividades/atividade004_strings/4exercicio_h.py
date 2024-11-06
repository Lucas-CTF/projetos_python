#Faça um programa que leia o nome de um aluno e mostre quantas vezes a 
# letra 'o' aparece e em que posição ela aparece pela primeira e última vez.

#IMPORTAÇÕES
import os

#LIMPEZA DO TERMINAL
os.system('cls')

#ENTRADA
nome = input('Me diga seu nome: ')
print()

#PROCESSAMENTO
nome_novo = nome.lower()
quantiaO = nome_novo.count('o')
inicio = nome_novo.find('o')
fim = nome_novo.rfind('o')

#SAIDA FORMATADA
if 'o' in nome or "O" in nome:
    print(f'Em {nome} a letra "o" apararece {quantiaO} vezes')
    print(f'Onde aparece no inicio: {inicio}')
    print(f'Onde aparece no fim: {fim}')
else:
    print("Não aparece a letra 'o' no seu nome! ")
    
print()