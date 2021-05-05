import numpy as np
from numpy import linalg as la
import os

clean = lambda: os.system('cls')

def Dot_f(a,b):
	return a.T*b.conjugate()

def Norm_f(x):
	return np.sqrt(Dot_f(x,x))	

def error_esc(a,b):
	return abs(a-b)/abs(b)*100

def error_vec(a,b):
	return Norm_f(a-b)/Norm_f(b)*100	


def power_method(A, x_old):
    e_old   = x_old
    lam_old = 0
    for k in range(200):
        x_new   = A*x_old
        lam_new   = Dot_f(x_new,x_old)/(Norm_f(x_old)**2)
        error_por = error_esc(lam_old,lam_new)
        e_new   = x_new/Norm_f(x_new)
        error_e = error_vec(e_old,e_new)
        lam_e     = Dot_f(e_new,A*e_new)/(Norm_f(e_new)**2) 
        error_lam = error_esc(lam_e,lam_new)
        error_eigen = error_vec(A*e_new/lam_new,e_new)
        x_old   = x_new
        lam_old = lam_new
        e_old   = e_new	
    print('eigenvalor:', lam_new[0,0])
    print('error lamda:', error_lam)
    print('eigenvector:', x_new)
    print('error vector:',error_e)
    print('----'*20)
    return A, x_new, lam_new

def matrix_deflation(A,x,lam):

    v = x/la.norm(x)
    R = v@v.T
    R = lam * R
    A = A - R
    return A

def run():
    A = np.matrix([[2   ,     0   , 0],
	            [0.5 , 5 , 0 ],
	            [-1.5, 1.0     , -1.0]])


    x = np.matrix([[2],
                    [2],
                    [2]])

    eigenvalues = []
    clean()
    w,v = la.eig(A)
    print(w)
    for i in range(len(A)):
        A, x_new, lam_new = power_method(A,x)
        #print('A:',A,'x: ',x_new, 'lam:',lam_new)
        #print('x:', x_new)
        #print('lam', lam_new[0,0])
        eigenvalues.append(lam_new[0,0])
        A = matrix_deflation(A, x_new, lam_new[0,0])
    
    print('Eigenvalores: ')
    print(eigenvalues)
    
if __name__ == "__main__":
    run()