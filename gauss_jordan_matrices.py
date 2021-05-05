import numpy as np
from numpy import linalg as LA
import os

clear = lambda: os.system('cls')

def sum_matrix(m1,m2):
    new_matrix = []
    assert len(m1) == len(m2), "Las dimensiones de las matrices no coinciden."

    for i in range(len(m1)):
        rows = []
        for j in range(len(m1)):
            rows.append(m1[i][j]+m2[i][j])
        new_matrix.append(rows)

    #print(new_matrix)
    return new_matrix

def augmented_matrix(m):
    z = zero_augmented(m)

    for i in range(len(m)):        
        for j in range(len(m)):
            z[i][j] = m[i][j]
            if i == j:
                z[i][j+len(m)] = 1
    return z

def zero_augmented(m):
    augmented = np.zeros((len(m),len(m)*2))
    return augmented


def gauss_elimination(m,n):
    for i in range(n):
        assert m[i][i] != 0.0, "No se puede dividir por cero."
            
        for j in range(n):
            if i != j:
                pivot = m[j][i]/m[i][i]

                for k in range(2*n):
                    m[j][k] = m[j][k] - pivot * m[i][k]
    
    for i in range(n):
        div = m[i][i]
        for j in range(2*n):
            m[i][j] = m[i][j]/div

    return m

def inverse_part(m,n):
    inverse = []
    for i in range(n):
        rows = []
        for j in range(n, 2*n):
            rows.append(m[i][j])
        inverse.append(rows)
    return inverse

def inverse_matrix(m):
    m_order = len(m)
    m = augmented_matrix(m)
    m = gauss_elimination(m,m_order)
    m = inverse_part(m,m_order)
    m = np.array(m)
    print("---"*30)
    print('matriz inversa:')
    print(m)
    print("---"*30)
    return m

def verification(m,inv_m):
    m = np.array(m)
    inv_m = np.array(inv_m)
    return np.dot(m,inv_m)

def run():
    D =[[2,0,0],
        [0,4,0],
        [0,0,6]]
    L =[[0,0,0],
        [2,0,0],
        [4,8,0]]

    clear()
    D_L = sum_matrix(L,D)
    inv_D_L = inverse_matrix(D_L)
    print('A * inv_A:')
    print(verification(D_L,inv_D_L))


if __name__ == '__main__':
    run()