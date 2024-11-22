import os


os.system('cls')

#Lista original
lista = [1, 2, 3, 4]

#Mostrando a lista original
print("Lista original:", lista)

#Pedindo ao usuario o elemento da lista
elemento = input('Elemento a ser removido: ')

#Tentando remover o elemento da lista
if elemento.isdigit():
    elemento = int(elemento) #Converte para inteiro se for um numero
if elemento in lista:
    lista.remove(elemento)
    print("Lista após a remoção:", lista)
else:
    print("Elemento não encontrado na lista.")