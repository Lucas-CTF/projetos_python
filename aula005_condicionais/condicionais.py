import os

os.system('cls')

print('-'*70)
print('Estudo de Condicional: parte 1')
print('-'*70)

#entrada de dados
numero = float(input('Digite um numero: '))
#isso é mais jeito, ta declarando uma variavel vazia, sem valor
resposta = ''

#condicional
#se for verdadeiro executa o de baixo
if numero % 2 == 0:
    resposta = f'O numero {numero} é par'
#se nao for verdadeiro executa esse
else:
    resposta = f'O numero {numero} é impar'
    
#saida
print('='*70)
print(resposta)

print('fim do programa!\n')   