import numpy as np
import sys 
from numba import jit
from numpy import linalg as LA
import matplotlib.pyplot as plt

sys.path.append('/home/mating/Documents/numerical_analysis_master/programs/tarea1')
from Sust import Sust
from invertion import Invertion

#@jit(nogil=True,fastmath=True,nopython=True)

A=np.array([[0.0,1.0],[1.0,1.0]])
y=np.array([1.0,2.0])
x0=np.array([1.0,1.0])

b=range(2,20,2)
deltas=[]
results=[]; cond=[]; x1=[]; x2=[]

for i in b:
	d=0.0; 
	d=10**-i

	deltas.append(d)
	A[0][0]=d

	method=Invertion(A)
	L,U=method.LU()

	S=Sust(L,U)
	y=S.sustDelante(y)
	x=S.sustAtras(y)
	results.append(LA.norm(x-x0))
	x1.append(x[0])
	x2.append(x[1])

	cond.append(LA.cond(A,2))


	
plt.scatter(deltas,results,marker='s')
plt.title("Estabilidad")
plt.xlabel("$\delta$")
plt.ylabel("$||x-x_{0} ||_{2}$")
plt.xlim([1e-18,0.01])
plt.xscale('log')
plt.yscale('log')
plt.grid()
plt.show()

plt.scatter(b,cond,marker='s')
plt.title("Comportamiento del número de condición")
plt.xlabel("Iteraciones")
plt.ylabel("Número de condición")
#plt.axhline(y=1, color='red',lw=3)
plt.ylim([2.60,2.7])
plt.grid()
plt.show()




