import os


os.system('cls')

#Inicializada a lista vazia
lista_numeros = [100, 200]

#Solicita ao usuario para inserir números separados por espaço
entrada = input("Digite numeros separados por espaço: ")

#Divide a string de entrada em uma lista de strings
numeros = entrada.split()

#Cria uma lista para armazenar os numeros pares
pares = []

#Itera sobre os numeros inseridos
for numero in numeros:
    #Converte a string para inteiro
    numero_aux = int(numero)
    #Verifica se o numero é par
    if numero_aux %2 ==0:
        #Adicionao numero par à lista de pares
        pares.append(numero_aux)
print('-'*70)
print(f'Lista gerada: {pares}')
print('-'*70)

#Usa extend() para adicionar todos os numeros pares à lista principal
lista_numeros.extend(pares)

#Exibe a lista resultante
print(f'Numeros pares adicionados à lista: {lista_numeros}')