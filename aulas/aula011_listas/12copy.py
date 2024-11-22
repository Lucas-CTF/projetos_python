import os


os.system('cls')

#Solicita ao usuario para inserir numeros separados por espaço
entrada = input("Digite numeros separados por espaços: ")

#Divide a string de entrada em uma lista de strings
numeros_str = entrada.split()

#Converte a lista de strings em uma lista de inteiros
numeros = []
for num_str in numeros_str:
    numeros.append(int(num_str))

#Solicita ao usuario para decidir se deseja
#criar uma copia da lista
escolha = input("Deseja criar uma copia? (s/n): ").strip().lower()

#Verifica a escolha do usuario e cria uma copia da
#lista se a resposta for 's'
if escolha == 's':
    lista_copiada = numeros.copy()
    print(f'Cópia da lista: {lista_copiada}')
else:
    print("A lista não foi copiada")

#Exibe a lista fornecida para referencia
print(f'Lista fornecida: {numeros}')