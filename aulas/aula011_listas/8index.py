import os


os.system('cls')

#Solicita ao usuario para inserir numeros separados por espaço
entrada = input('Digite numeros seprados por espaço: ')

#Divide a string de entrada em uma lista de strings
numeros_str = entrada.split()

#Converte a lista de strings em uma lista de inteiros
numeros = []
for num_str in numeros_str:
    numeros.append(int(num_str))

#Solicita ao usuario para inserir o numero que deseja encontrar na lista
busca_numero = int(input('Digite o numero que deseja encontrar: '))

#Tenta encontrar o indice do numero fornecido
if busca_numero in numeros:
    indice = numeros.index(busca_numero)
    print(f'O numero {busca_numero} esta no indice {indice}')
else:
    print(f'O numero {busca_numero} nao foi encontrado na lista.')

#Exibe a lista fornecida para referencia
print(f'Lista fornecida: {numeros}')