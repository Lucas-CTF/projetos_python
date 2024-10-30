#C) A empresa "SafeDrive" está desenvolvendo um sistema de monitoramento de velocidade para ajudar a promover a segurança nas estradas. 
#Eles precisam de um programa que permita aos usuários inserir a velocidade de um carro e, em seguida, exibir na tela uma mensagem adequada com base na velocidade fornecida. 
# O objetivo principal é alertar os motoristas caso ultrapassem o limite de velocidade de 60 km/h, incentivando-os a dirigir dentro dos limites legais e, assim, 
# reduzir o risco de acidentes.

import os


os.system('cls')

print('=' *70)
print('RESPEITE OS LIMITES DE VELOCIDADE')
print('=' *70)
print()

#entrada de dados
velocidade = int(input('Insira a velocidade do seu carro em km/h: '))
print()

#string vazia para receber valores
resposta = ''

if 30 <= velocidade <= 60:
    resposta = f'A velocidade {velocidade} está adequada, continue assim!'
elif velocidade > 60:
    resposta = f'A velocidade {velocidade} está acima do limite, REDUZA!'
else:
    resposta = f'A velocidade {velocidade} está abaixo do minimo aceito, aumente!'

#saida
print(resposta)
print()

