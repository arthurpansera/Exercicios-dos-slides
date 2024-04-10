#Crie um algoritmo que peça ao usuário para informar 5 valores inteiros positivos
#Armazene-os em uma lista com nome qualquer
#Em seguida, crie uma nova lista ordenada dos valores
#Crie uma nova lista com os valores ordenados em ordem inversa
#Imprima as três listas, o tamanho da lista, o menor valor informado, o maior valor informado, a soma de todos os valores da lista

lista = []

for i in range(5):
    numeros = int(input(f"Informe o {i+1}º número: "))
    i += 1
    lista.append(numeros)

print(lista)
print(50*"-")