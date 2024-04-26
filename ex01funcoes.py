#Imprimir nome
#Definição da função como bloco
"""def imprimir_nome():
    nome = input("Informe seu nome:\n")
    print(f"O nome é: {nome}")

imprimir_nome()"""

#Definição da função como parâmetro
"""def imprimir_nome(nome):
    print(f"O nome é: {nome}")

n = input("Informe o nome:\n")
imprimir_nome(n)"""

#Função para pedir nome
def pedir_nome():
    nome = input("Informe o nome:\n")
    return nome

nome = pedir_nome()
print(f"O nome é: {nome}") #Há outra forma: print(f"O nome é: {pedir_nome()}")