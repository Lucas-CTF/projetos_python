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

#Solicita ao usuario para decidir se deseja limpar a lista
escolha = input("Deseja limpar a lista? (s/n): ").strip().lower()

#Exibe a lista fornecida para referencia
print(f'Lista fornecida: {numeros}')

#Verifica a escolha do usuario e limpa a lista se a resposta for 's'
if escolha == 's':
    numeros.clear()
    print(f'Lista limpa: {numeros}')
else:
    print("A lista não foi limpa.")