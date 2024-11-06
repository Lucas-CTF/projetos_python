#H) A empresa "RootCalc" está desenvolvendo um software de cálculo de raízes de equações quadráticas para auxiliar engenheiros e cientistas em suas análises e projetos. 
# Eles precisam de um programa que calcule as raízes da equação quadrática 𝑥²−6𝑥+5 sem depender de funções ou métodos predefinidos, utilizando apenas os conceitos e operações 
# básicas aprendidos até o momento. Essas raízes são conhecidas como 𝑥’ = 5 e 𝑥’’ = 1, e o programa deve ser capaz de calcular essas raízes de forma precisa, seguindo os 
# princípios matemáticos fundamentais.

#importando biblioteca
import os

#usando comando da biblioteca para limpar o terminal
os.system('cls')

#TITULO
print('='*70)
print('VAMOS CALCULAR A FUNÇÃO QUADRATICA "𝑥²−6𝑥+5" E DESCOBRIR SUAS RAIZES')
print('='*70)
print()

#DECLARAÇÕES
a = 1
b = -6
c = 5

#PROCESSAMENTO
delta = ((b**2) - 4 * a * c)
raizdedelta = delta ** 0.5
raiz1 = (-b - raizdedelta) / (2 * a)
raiz2 = (-b + raizdedelta) / (2 * a)

#SAIDA
print(f'Suas raizes são {raiz1}, {raiz2}')
print()