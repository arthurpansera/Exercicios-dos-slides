#Imprimir os elementos de um vetor qualque
#Criando um vetor:
vetor = ["Clemer","Kléber","Índio","Bolivar","Nei","Guiñazu","Figueroa","Falcão","D'alessandro","Carlitos","Fernandão"]
for jogador in vetor:
    print(jogador)

#Vamos fazer a mesma coisa
#Fazendo de outra forma (caso precise do índice)
for i in range(0,len(vetor)):
    print(f"Elemento {i+1}: Valor: {vetor[i]}")