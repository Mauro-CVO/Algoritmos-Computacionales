import numpy as np
from numpy import linalg as al

from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt

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
    epsilon = 1e-2
    error_x = 1000
    vect_lst = [x_0]
    error_lst = []
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
        vect_lst.append(x_new)
        print(x_new)
        error_x = fact_error*al.norm(x_new-x_old)
        error_lst.append(error_x)
        print("Error de aprox:", error_x)
        print("----" * 20)
    error_lst.append(0)

    #error_lst /= np.max(error_lst)

    #fig = plt.figure()
    #ax = plt.axes(projection = '3d')
    #for i in range(len(vect_lst)):
    #    p = vect_lst[i]
    #    ax.scatter3D(p[0,0],p[1,0],p[2,0]), color =(0.5,0.5,0.5)
    #    ax.text(p[0,0],p[1,0],p[2,0], str(i))
    #plt.show()

if __name__ == '__main__':
    run()