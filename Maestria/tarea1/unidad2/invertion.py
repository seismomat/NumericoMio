import numpy as np 
import math 

class Invertion:
  ## A es un numpy array de dos dimensiones

  def __init__(self, A):
    self.A=A

  def LU(self):
    n=len(self.A) # dimension del arreglo 

    self.L=np.identity(n) # matriz identidad
    self.U=np.copy(self.A) # el primer paso es U=A

    for i in range(0,n):
      for j in range(i+1,n):

        factor= self.U[j][i]/ self.U[i][i]
        self.L[j][i]=factor

        for k in range(i,n):
          self.U[j][k]= self.U[j][k]- factor*self.U[i][k]

          #U[1][1] - factor * U[0][1]

    return self.L,self.U

  
  def QR(self):

    self.Q=np.empty_like(self.A) ## matriz Q
    self.R=np.zeros([self.A.shape[1],self.A.shape[1]]) ## matriz cuadrada

    vi=np.zeros([self.A.shape[1]])

    for i in range(self.A.shape[1]):
        vi=self.A[:,i]

        for j in range(i):
          self.R[j,i]=np.dot(self.Q[:,j].T,vi)
          vi = vi - self.R[j,i]*self.Q[:,j]
          #vi = a2 - (q1T, a2)* q1


        self.R[i,i]=np.linalg.norm(vi,2)
        self.Q[:,i]=vi/self.R[i,i]


    return self.Q,self.R


  def ElimGauss(self):  
    N=self.A.shape[0]

    for k in range(N):
      pivot=self.A[k][k];
      for j in range(k,N+1):
        self.A[k][j]=self.A[k][j]/pivot;
      for i in range(N):
        if i != k:
          d=self.A[i][k];
          for m in range(k,N+1):
            self.A[i][m]=self.A[i][m]-d*self.A[k][m];
    for i in range(N):
      print("x[%d]=%lf\n"%( i+1, self.A[i][N]));

    print(self.A)
    return 




 
  def Cholesky(self):
    n=self.A.shape[0]
    self.L=np.zeros_like(self.A)

    for k in range(n):
      for i in range(k+1):
        if k==i:
          sum=0.0
          for j in range(k):
            sum+= self.L[k][j]*self.L[k][j]
          self.L[k][k]=np.sqrt(self.A[k][k]-sum)

        else:
          sum=0.0
          for j in range(i):
            sum+= self.L[i][j]*self.L[k][j]
          self.L[k][i]=(self.A[k][i]-sum)/self.L[i][i]



    return self.L