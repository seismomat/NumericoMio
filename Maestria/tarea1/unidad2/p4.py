import numpy as np
import sys 
from numba import jit
from numpy import linalg as LA
import matplotlib.pyplot as plt
from scipy.linalg import hilbert

sys.path.append('/home/mating/Documents/numerical_analysis_master/programs/tarea1')
from Sust import Sust
from invertion import Invertion

#@jit(nogil=True,fastmath=True,nopython=True)


nn=range(2,21)
deltas=[]
cond=[];

for n in nn:

	H=hilbert(n)
	x=np.ones(n)
	b=H@x 


	method=Invertion(H)
	L=method.Cholesky()
	Lt=L.T
	S=Sust(L,Lt)
	y=S.sustDelante(b)
	x_g=S.sustAtras(y)
	deltas.append(LA.norm(x-x_g,np.Inf))

	cond.append(LA.cond(H,np.Inf))


	
plt.scatter(nn,deltas,marker='s')
#plt.xlim([1e-18,0.01])
plt.xscale('log')
plt.yscale('log')
plt.title("Error absoluto")
plt.xlabel("Tamaño de la matriz")
plt.ylabel("$||x-x_{0} ||_{\infty}$")
plt.grid()
plt.show()

plt.scatter(nn,cond,marker='s')
#plt.axhline(y=1, color='red',lw=3)
plt.title("Comportamiento del número de condición")
plt.xlabel("Iteraciones")
plt.ylabel("Número de condición")
plt.grid()
plt.yscale('log')
#plt.ylim([2.60,2.7])
plt.show()