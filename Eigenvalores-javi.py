import numpy as np
from numpy import linalg as la

### Funciones
def Dot_f(a,b):
	return a.T*b.conjugate()

def Norm_f(x):
	return np.sqrt(Dot_f(x,x))	

def error_esc(a,b):
	return abs(a-b)/abs(b)*100

def error_vec(a,b):
	return Norm_f(a-b)/Norm_f(b)*100	
######################################

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

A = np.matrix([[2   ,     0   , 0],
	            [0.5 , 5 , 0 ],
	            [-1.5, 1.0     , -1.0]])


x_old = np.matrix([[1],
                [1],
                [1]])

autovalores = []

w,v = la.eig(A)
print(w)

#for i in range(len(A)):
#    A, x_new, lam_new = power_method(A,x)
#    #print('A:',A,'x: ',x_new, 'lam:',lam_new)
#    #print('x:', x_new)
#    #print('lam', lam_new[0,0])
#    autovalores.append(lam_new[0,0])
#    A = matrix_deflation(A, x_new, lam_new[0,0])
    
print('Eigenvalores: ')
print(autovalores)

for i in range(len(A)):
    e_old   = np.matrix([[1],[1],[1]])
    lam_old = 0
    for k in range(50):
        k += 1
        #print(k) 
        x_new   = A*x_old

        lam_new   = Dot_f(x_new,x_old)/(Norm_f(x_old)**2)
        error_por = error_esc(lam_old,lam_new)
        print("----"*15)
        print("Iteración "+str(k))
        print("  lam_"+str(k)+" = ", lam_new)
        print("  error % =", error_por)
        print()
        print("...."*10)

        e_new   = x_new/Norm_f(x_new)
        error_e = error_vec(e_old,e_new)
        print("  e_k = ",e_new)
        print("  error_v % =", error_e)
        print("...."*10)

        lam_e     = Dot_f(e_new,A*e_new)/(Norm_f(e_new)**2) 
        error_lam = error_esc(lam_e,lam_new)
        print("  lam_e_"+str(k)+" = ", lam_e)
        print("  error_lam % =", error_lam)
        error_eigen = error_vec(A*e_new/lam_new,e_new)
        print("  error_eigen % =", error_eigen)
        x_old   = x_new
        lam_old = lam_new
        e_old   = e_new	

    autovalores.append(lam_new[0,0])

    v = x_new/la.norm(x_new)
    R = v@v.T
    R = lam_new[0,0] * R
    A = A - R

print(autovalores)


