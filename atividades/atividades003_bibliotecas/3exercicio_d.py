#Faça um programa que receba um ângulo qualquer. Em seguida, calcule o seno, cosseno e tangente do ângulo, limitando a saída a 2 casas decimais.
import os
import math


os.system('cls')

print('='*70)
print('SENO, COSSENO, TANGENTE')
print('='*70)
print()

graus = int(input('Me diga quantos graus tem o angulo: '))
print()

#as funções de math calculam os angulos usando radianos e não graus, por isso precisamos converter antes de fazer os calculos
radians = math.radians(graus)

#fazendo os calculos usando radianos
seno = math.sin(radians)
cosseno = math.cos(radians)
tangente = math.tan(radians)

#não precisamos converter os valores, pois o seno etc, tanto para radianos e graus sera o mesmo, e não tem 'medida'

#normalmente separo em linhas diferentes os resultados para facilitar, porem quero me desafiar e fazer tudo em uma linha só
#Usamos "\n" para pular uma linha, e usamos "\" para dizer que a linha de baixo faz parte da de cima
print(f'Resultados:\nSeno = {seno:.2f}\nCosseno = {cosseno:.2f}\n\
Tangente: {tangente:.2f}')
print()