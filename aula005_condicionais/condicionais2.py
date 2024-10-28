import os

os.system('cls')

#declarações
a = 10
b = 5
resposta = ''

print('-'*70)
print('Estudo de Condicional: parte 2')
print('-'*70)
print()

print('-'*70)
print('Estudo de Condicional (simples)')
print('-'*70)

#condicionais
if a > b:
    resposta = f'{a} é maior que {b}'
else:
    resposta = f'{a} não é maior que {b}'

#saida
print('-' * 70)
print(resposta)
print()

#declarações
a = 5
b = 5 
print('-'*70)
print('Estudo de Condicional (aninhada)')
print('-'*70)
print()
if a > b:
    resposta = f'{a} é maior que {b}'
elif a < b:
    resposta = f'{a} é menor que {b}'
else:
    resposta = f'Os valores são iguais: {a} = {b}'
    
#saida
print('-' *70)
print(resposta)
print('-' *70)
print()