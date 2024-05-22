#Crie uma matriz de tamanho 3x3 e preencha-a com valores de 1 a 9.
#Imprima a matriz das três formas:
#1. print(matriz)
#2. utilizando um for
#3. utilizando dois for's

matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print("\n")

print(matriz)

#for linha in matriz:
    #print(linha)

#for i in range(len(matriz)):
    #print(matriz[i])

print("\n")

#linha = i, coluna = j
for linha in range(3):
    print(matriz[linha])
print("\n")

for linha in range(3):
    for coluna in range(3):
        print(matriz[linha][coluna])
print("\n")