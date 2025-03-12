import numpy as np
#Exercicios 4
#1-

arr1 = np.ones(8, dtype=int)
arr_rand = np.random.randint(0, 10, size=8)

arr_final = arr1 + arr_rand
soma = np.sum(arr_final)

# Remodelando o array
if soma >= 40:
    matrix_nova = arr_final.reshape(4, 2)  # Mais linhas do que colunas
else:
    matrix_nova = arr_final.reshape(2, 4)  # Mais colunas do que linhas

# 2-

array_pares1 = np.arange(0, 52, 2)  # De 0 a 51
array_pares2 = np.arange(100, 48, -2)  # De 100 a 50

array_conc = np.concatenate((array_pares1, array_pares2))
array_ord = np.sort(array_conc)

print(array_ord)

# 3-

# Criando matriz 2x2 com zeros
camp_mina = np.zeros((2, 2), dtype=int)

# Adicionando o número 1 em uma posição aleatória
linha, coluna = np.random.randint(0, 2, size=2)
camp_mina[linha, coluna] = 1

# Jogo
tentativas = 0
while tentativas < 3:
    print("Matriz Atual:")
    print(camp_mina)
    x = int(input("Escolha a linha (0 ou 1): "))
    y = int(input("Escolha a coluna (0 ou 1): "))

    if camp_mina[x, y] == 1:
        print("KAAAAAAAABOOOOOOOMMMMMMM")
        break

    tentativas += 1
    if tentativas == 3:
        print("desarmoou")

# 4-
matriz = np.random.randint(0, 10, size=(3, 4))

linhas, colunas = matriz.shape

num_elementos = linhas * colunas
print("podera ser um vetor de elementos: ")
par_ou_impar = "par" if num_elementos % 2 == 0 else "ímpar"


# 5-

np.random.seed(10)
matriz_4x4 = np.random.randint(1, 51, size=(4, 4))

medias_linhas = np.mean(matriz_4x4, axis=1)
medias_colunas = np.mean(matriz_4x4, axis=0)

maior_media_linhas = np.max(medias_linhas)
maior_media_colunas = np.max(medias_colunas)

valores, contagens = np.unique(matriz_4x4, return_counts=True)
apareceu = dict(zip(valores, contagens))

numeros_repetidos_2x = [num for num, cont in apareceu.items() if cont == 2]

# Exibindo os resultados
print("Matriz 4x4 gerada:\n", matriz_4x4)
print("Médias das linhas:", medias_linhas)
print("Médias das colunas:", medias_colunas)
print("Maior média das linhas:", maior_media_linhas)
print("Maior média das colunas:", maior_media_colunas)
print("Contagem de aparições dos números:", apareceu)
print("Números que aparecem exatamente 2 vezes:", numeros_repetidos_2x)
