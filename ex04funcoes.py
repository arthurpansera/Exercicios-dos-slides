#Receber uma lista de números e retornar a média

def calcular_media(lista_notas):
    soma = 0
    for nota in lista_notas:
        soma += nota
    media = soma/len(lista_notas)
    return media

#lista = [7,10,5]
#print(f"A média da lista {lista} é {media}")

nota = 0
listaNotas = []
while nota != -1:
    nota = int(input("Informe a nota ou digite -1 para encerrar: "))
    if nota == -1:
        continue
    elif nota < 0 or nota > 10:
        print("Nota inválida!")
        continue
    else:
        listaNotas.append(nota)

print(f"A média é {calcular_media(listaNotas):.2f}")