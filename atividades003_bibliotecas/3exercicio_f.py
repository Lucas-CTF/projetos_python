#Faça um programa onde o usuário tenta adivinhar o número que o computador está ‘pensando’.
#importando bibliotecas
import os
import random


#limpando terminal
os.system('cls')

#Titulo do programa
print('='*70)
print('Tente adivinhar')
print('='*70)
print()

#criando numero aleatorio
sorteado = random.randint(1, 20)

#entrada
num = int(input('Tente adivinhar o numero que pensei, entre 1 e 20: '))
print()

#checando a respota do usuario
if num == sorteado:
#saida
	print(f'Parabens você acertou! O numero é {sorteado}')
else:
	print(f'Que pena você errou! O numero não é {num} ')
	print(f'O numero certo era {sorteado}')

print()
