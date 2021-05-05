import numpy as np
from numpy import linalg as al

from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt

def run():
    A = np.matrix([[5,-2,3],
                    [-3,9,1],
                    [2,-1,-7]])

    b = np.matrix([[-1],[5],[3]])

    x_0 = np.matrix([[1],[1],[1]])
    #-----------------------------------#
    n = np.shape(A)[0]
    U = np.triu(A,1)
    L = np.tril(A,-1)
    D = A-U-L
    
    #------------------------------------------###
    M_inverse = al.inv(L+D)
    B = -M_inverse*U
    d = M_inverse * b
    
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
    ###'''
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