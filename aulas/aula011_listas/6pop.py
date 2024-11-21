import os


os.system('cls')

#Inicializada uma lista de exemplo
lista_numeros = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

#Solicita ao usuario para inserir um indice para remover o elemento
indice = int(input('Digite o indice do elemnto a ser removido (0-9): '))

#Verifica se o indice esta dentro do intervalo vaálido da lista
if 0 <= indice < len(lista_numeros):
    #Remove o elemento no indice especificado e exibe-o
    elemento_removido = lista_numeros.pop(indice)
    print(f'Elemento removido: {elemento_removido}')
else:
    print('Indice invalido!')

#Exibe a lista resultante
print("Lista após remoção:", lista_numeros)