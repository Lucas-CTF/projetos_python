import os
import datetime

os.system('cls')

print('='*28)
print('Entrada de Dados')
print('='*28)

print()

#Entrada
nome = input('Me diga seu nome: ')
peso = input('Seu peso: ')
altura = input('Sua altura: ')

#Entrada com casting
nascimento = int(input('Data de Nascimento: '))
cep = int(input('Seu CEP: '))
bairro = input('Me diga seu Bairro: ')
rua = input('Sua rua:')
numero = input('Seu numero: ')

#Aqui vai só pegar o ano atual e calcular a idade da pessoa
ano_atual = datetime.datetime.now().year
idade = int(ano_atual) - nascimento

print()

print('='*28)
print('Saida de Dados')
print('='*28)

print()

#saida normal
print('Nome: ', nome)
print('Ano de nascimento: ', nascimento)
print('Peso: ', peso)
print('Altura: ', altura)

#Saida interpolada
print(f'{nome}, você tem {idade} anos!')
print(f'CEP: {cep}')
print(f'Bairro: {bairro}')
print(f'Rua: {rua}')
print(f'Numero: {numero}')
print('='*28)