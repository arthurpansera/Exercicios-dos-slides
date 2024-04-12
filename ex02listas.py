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

print(50*"-")
print(lista)
print(50*"-")
lista.sort()
print(lista)
print(50*"-")
lista.reverse()
print(lista)
print(50*"-")
print(f"O total de valores da lista é: {len(lista)}")
print(f"O menor valor da lista é: {min(lista)}")
print(f"O maior valor da lista é: {max(lista)}")
print(f"O resultado da soma de todos os valores da lista é: {sum(lista)}")
print(50*"-")