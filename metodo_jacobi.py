import numpy as np
from numpy import linalg as al

def factor_error(norm_B):
    return norm_B/(1-norm_B)

def d_vector(E,b):
    return E*b

def elemental(E,A,n):
    for i in range(n):
        E[i,i] = 1/A[i,i]
    return E

def B_matrix(E,A,I):
    return I-E*A

def run():
    A = np.matrix([[5,-2,3],
                    [-3,9,1],
                    [2,-1,-7]])

    b = np.matrix([[-1],[5],[3]])

    x_0 = np.matrix([[1],[1],[1]])
    
    n = np.shape(A)[0]
    E = np.identity(n)
    I = np.identity(n)
    
    E = elemental(E,A,n)
    B = B_matrix(E,A,I)
    norm_B = al.norm(B)
    d = d_vector(E,b)

    fact_error = factor_error(norm_B)

    #x_1 = B*x_0 + d
    #error_x = fact_error*al.norm(x_1-x_0)
    
    #for i in range(int(input('numero de iteraciones: '))):
    #    if i == 0:
    #        x_old = x_0
    #        x_new = B*x_old + d
    #    else:
    #        x_old = x_new
    #        x_new = B*x_old + d
    #    print(x_new)
    #    error_x = fact_error*al.norm(x_new-x_old)
    #    print("Error de aprox:", error_x)
    #    print("----" * 20)
    
    #-----------------------------------------------------------#
    epsilon = 1e-4
    error_x = 1000
    k = 0
    print(epsilon)
    while k < 100 and epsilon < error_x:
        print(k)
        if k == 0:
            x_old = x_0   
            x_new = B*x_old + d
        else:
            x_old = x_new
            x_new = B*x_old + d
        k += 1
        print(x_new)
        error_x = fact_error*al.norm(x_new-x_old)
        print("Error de aprox:", error_x)
        print("----" * 20)

    

if __name__ == '__main__':
    run()