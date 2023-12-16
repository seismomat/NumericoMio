import numpy as np 
import math 
import sys 
sys.path.append('/home/mating/Documents/numerical_analysis_master/programs/tarea1')
from Sust import Sust
from numpy import linalg as LA


class Inversion:
  ## A es un numpy array de dos dimensiones

  def __init__(self, A):
    self.A=A

  def LU(self):
    n=len(self.A) # dimension del arreglo 

    self.L=np.identity(n) # matriz identidad
    self.U=np.copy(self.A) # el primer paso es U=A
    p=np.eye(n)
    p1=[];p2=[]

    for i in range(0,n):
      jj=i+1
      aux=p.copy()
      aux2=p.copy()
      while self.U[i][i]==0:
        self.U[[i, jj],:] = self.U[[jj, i],:]
        aux[[i, jj],:] = aux[[jj, i],:]
        jj+=1
        if jj==n and self.U[i][i]==0:
          raise Exception('No se puede llevar a cabo LU')
      p1.append(aux)
      for j in range(i+1,n):

        factor= self.U[j][i]/ self.U[i][i]
        aux2[j][i]=factor
        #self.L[j][i]=factor
        

        for k in range(i,n):
          self.U[j][k]= self.U[j][k]- factor*self.U[i][k]

          #U[1][1] - factor * U[0][1]
      #print("despues del for j")
      #print(self.U)
      auxx=aux@aux2
      #self.L=self.L@auxx
      p2.append(aux2)
      """
      print("jaja",i)
      print(auxx)
      print("jaje",i)
      print(aux2)
      print("jaji",i)
      print(aux)
      """

    c=p1[0]
    d=p1[0]@p2[0]
    for i in range(1,len(p1)):
      c=p1[i]@c
    for i in range(1,len(p1)):
      d=d@(p1[i]@p2[i])



    self.per=c
    self.L=d
    return self.L,self.U,self.per

AA= np.array([[0.0,0.0,0.0,1.0,1.0,1.0,0.0],[0.0,0.0,0.0,0.0,0.0,0.0,1.0],
  [1.0,0.0,0.0,1.0,0.0,0.0,1.0],[0.0,1.0,0.0,0.0,1.0,0.0,0.0],
  [0.0,0.0,1.0,0.0,0.0,1.0,0.0],[1.0,0.0,0.0,0.0,1.0,0.0,0.0],
  [0.0,0.0,1.0,0.0,1.0,0.0,1.0]])

# inciso A
print("Inciso A")
B=3*np.ones(7)

ob=Inversion(AA)
Lp,Up,pp=ob.LU()

S=Sust(Lp,Up)
y=S.sustDelante(B)
x=S.sustAtras(y)

print(" resultado inciso A")
print(pp@x)

# inciso B
Minv=np.zeros((7,7))
print("Inciso B")
for i in range(7):
  ei=np.zeros(7)
  ei[i]=1
  M=np.copy(AA)
  ob=Inversion(M)
  Li,Ui,ppi=ob.LU()

  S=Sust(Lp,Up)
  y=S.sustDelante(ei)
  x=S.sustAtras(y)
  Minv[:,i]=ppi@x

print(" resultado inciso B")

print(Minv)


print("Inciso C")

print(" número de condición con norma 1")
print(LA.cond(AA,1))

print(" número de condición con norma Infinito")
print(LA.cond(AA,np.Inf))
"""
print(" matrices")
print(Lp)
print()
print(Up)
print()
print(pp)
print()
print(pp@AA)
print()
print(Lp@Up)

"""