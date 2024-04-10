#Crie um algoritmo que possua duas listas vazias chamadas numerosJogador1 e numerosJogador2
#Em seguida, randomize um número entre 1 e 6 (vamos simular um dado) e armazene o valor na lista
#Repita esse processo 3 vezes (como se 3 dados tivessem sido jogados) para cada um dos jogadores
#Por último, some os valores de cada jogador, e exiba na tela qual jogador foi o vencedor
#Vence aquele que tiver a soma com maior número

import random
numerosJogador1 = []
numerosJogador2 = []
somaJogador1 = 0
somaJogador2 = 0

for i in range(3):
    numeros1 = random.randint(1,6)
    numerosJogador1.append(numeros1)
    somaJogador1 += numeros1
    numeros2 = random.randint(1,6)
    numerosJogador2.append(numeros2)
    somaJogador2 += numeros2

print(numerosJogador1)
print(numerosJogador2)
print(f"A soma dos valores do jogador 1 foi: {somaJogador1}")
print(f"A soma dos valores do jogador 2 foi: {somaJogador2}")

if somaJogador1 > somaJogador2:
    print("O jogador 1 venceu")
elif somaJogador1 == somaJogador2:
    print("Empate")
else:
    print("O jogador 2 venceu")