import numpy as np
import NormalsConics1 as Ns
from numpy import linalg as LA
import matplotlib.pyplot as plt

def fun(x,y,r,c):
    return np.sqrt(r**2-x-y)+c**2
x= [0.26 ,0.23 ,0.255 ,0.27 ,2.74 ,2.75 ,2.77 ,2.74 ,0.25 ,2.7 ,1.6 ,1.5]
x=np.array(x)
x=x.reshape((x.shape[0],1))
y=[1.9 ,1.92 ,4.5 ,4.42 ,1.92 ,1.92 ,4.4 ,4.45 ,3.3 ,3.2 ,1.93 ,4.5]
y=np.array(y)
y=y.reshape((y.shape[0],1))
z=[3.6,7,3.52,7.1,3.53,6.99,3.56,7.056,5.9,5.82,5.8,5.75]
z=np.array(z)
z=z.reshape((z.shape[0],1))

data={'x':x,'y':y,'z':z}

pol=Ns.NormalsConics(data)
Fit_data,r_2=pol.SolveHouseHolder()


M=pol.get_matrix()

print("coeficientes",Fit_data)
print("norma ", LA.norm(M,np.inf)-r_2)

X, Y = np.meshgrid(x, y)

X=(X-Fit_data[0])**2
Y=(Y-Fit_data[1])**2
zs = fun(np.ravel(X), np.ravel(Y),r_2,Fit_data[2])
Z = zs.reshape(X.shape)
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.scatter(x,y,z)
ax.plot_surface(X, Y, Z)

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
plt.show()


"""
res=LA.norm(M@Fit_data-y)

print("Residual con Cholesky:",res)

Fit_data1,M1=pol.SolveGrandSmith()

res1=LA.norm(M1@Fit_data1-y)

print("Residual con Cholesky:",res)
"""
