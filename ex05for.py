#Crie um vetor de 10 posições com números aleatórios (utilize o random do python
#Em seguida, solicite ao usuário um número inteiro qualquer
#Verifique se o número digitado existe no vetor

import random
vetor = [random.randint(1,10) for i in range(10)]

numero = int(input("Digite um número inteiro: "))
#Se o número existir, imprima: O número digitado foi X e existe na posição Y
#Se o número não existir, imprima : O número digitado foi X e não existe no vetor
if numero in vetor:
    posicao = vetor.index(numero)+1
    print(f"O número digitado foi {numero} e existe na posição {posicao}")
else:
    print(f"O número digitado foi {numero} e não existe no vetor")