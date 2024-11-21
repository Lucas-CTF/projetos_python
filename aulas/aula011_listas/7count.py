import os


os.system('cls')

#Solicita ao usuario para inserir numeros separados por espaço
entrada = input("Digite numeros separados por espaço: ")

#Divide a string de entrada em uma lista de strings
numeros_str = entrada.split()

#Converte a lista de strings em uma lista de inteiros
numeros = []
for num_str in numeros_str:
    numeros.append(int(num_str))

#Solicita ao usuario para inserir o numero que deseja contar na lista
numeros_para_contar = int(input('Digite o numero que deseja contar: '))

#Conta o numero de vezes que o numero fornecido aparece na lista
contagem = numeros.count(numeros_para_contar)

if contagem > 0:
    print(f'O numero {numeros_para_contar} aparece {contagem} vezes na lista')
else:
    print(f'O numero {numeros_para_contar} não aparece na lista.')

#Exibe a lista fornecida para referencia
print(f'Lista fornecida: {numeros}')