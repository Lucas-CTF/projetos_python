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

#Exibea lista fornecida para referencia
print("Lista fornecida:", numeros)

#Solicita ao usuario para decidir se deseja inverter a lista
escolha = input("Deseja inverter a ordem da lista? (s/n): ").strip().lower()

#Verifica a escolha do usuario e inverte a lista se a resposta for 's'
if escolha == 's':
    numeros.reverse()
    print("Lista invertida:", numeros)
else:
    print("A lista não foi invertida.")