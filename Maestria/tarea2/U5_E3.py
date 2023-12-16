import numpy as np
from numpy import linalg as LA

import EigenRay as ER


A= np.array([[0.0,1.0,-1.0],[1.0,1.0,0.0],[-1.0,0.0,1.0]])
A= np.array([[2.0,1.0,1.0],[1.0,3.0,1.0],[1.0,1.0,4.0]])
x0=np.array([1/np.sqrt(3),1/np.sqrt(3),1/np.sqrt(3)]).reshape((A.shape[0],1))
l0= x0.T@(A@x0)

data={'A':A,'x0':x0,'l0':l0,'n':100}
EiNew= ER.EigenRay(data)

xk,lk=EiNew.EigenR()

print("Eigenvector con método de Rayleigh \n ", xk)
print()
print("Eigenvalor con método de Rayleigh ",lk)
print()
W,V=LA.eig(A)
print("Eigenvalores con método de numpy \n",W)
print()
print("Eigenvectores con método de numpy \n",V)
