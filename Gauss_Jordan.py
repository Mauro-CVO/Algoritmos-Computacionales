import numpy as np

D =[[5,0,0],
    [0,8,0],
    [0,0,4]]
L =[[0,0,0],
    [8,0,0],
    [9,4,0]]

suma_D_L = []

# suma de la matriz D y L
for i in range(len(D)):
    filas = []
    for j in range(len(L)):
        filas.append(D[i][j]+L[i][j])
    suma_D_L.append(filas)

tamano_D_L = len(suma_D_L)

# matriz aumentada
matriz_aumentada = np.zeros((tamano_D_L,tamano_D_L*2))

for i in range(tamano_D_L):        
    for j in range(tamano_D_L):
        matriz_aumentada[i][j] = suma_D_L[i][j]
        if i == j:
            matriz_aumentada[i][j+tamano_D_L] = 1
print('matriz aumentada: ')
print(matriz_aumentada)
print("---"*20)
#eliminacion gaussiana

for i in range(tamano_D_L):
        for j in range(tamano_D_L):
            if i != j:
                pivote = matriz_aumentada[j][i]/matriz_aumentada[i][i]
                for k in range(2*tamano_D_L):
                    matriz_aumentada[j][k] = matriz_aumentada[j][k] - pivote * matriz_aumentada[i][k]

for i in range(tamano_D_L):
    pivote = matriz_aumentada[i][i]
    for j in range(2*tamano_D_L):
        matriz_aumentada[i][j] = matriz_aumentada[i][j]/pivote
print('eliminacion gaussiana: ')
print(matriz_aumentada)
print("---"*20)
# matriz inversa

D_L_inversa = []
print('matriz inversa: ')
for i in range(tamano_D_L):
    filas = []
    for j in range(tamano_D_L, 2*tamano_D_L):
        filas.append(matriz_aumentada[i][j])
    print(filas)
    D_L_inversa.append(filas)

print("---"*20)

    