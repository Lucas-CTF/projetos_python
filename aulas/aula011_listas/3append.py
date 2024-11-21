import os


os.system('cls')

#Inicializa uma lista vazia
lista_numeros = []

#Pede ao usuario para inserir tres numeros
for i in range(3):
    numero = int(input("Digite um numero: "))

    #Adiciona o numero à lista
    lista_numeros.append(numero)

print(f'Lista gerada: {lista_numeros}')
#Verifica se o numero inserido está na lista e 
#exibe uma mensagem
print('-'*70)
numero_verificar = int(input("Numero para busca: "))
print('-'*70)

if numero_verificar in lista_numeros:
    print(f'O numero {numero_verificar} esta na lista!')
else:
    print(f'O numero {numero_verificar} não esta na lista!')