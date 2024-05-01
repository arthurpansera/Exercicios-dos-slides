#Receber uma lista de números e retornar a média

def calcular_media(listaNumeros):
    soma = 0
    for num in listaNumeros:
        soma += num
    return soma/len(listaNumeros)

lista = [7,10,5]
media = calcular_media(lista)
print(f"A média da lista {lista} é {media}")