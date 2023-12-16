import numpy as np
from numpy import linalg as LA
import Tools as Ts
from numba import jit

#@jit(nogil=True,fastmath=True,nopython=True)
class FactGivens:
    def __init__(self,A):
        self.A=A # original matrix
        self.rows=self.A.shape[0] # rows
        self.col=self.A.shape[1] # columns
        self.min=np.minimum(self.col,self.rows-1) # minimum between
        # columns and rows
        self.R=np.copy(self.A)

    def Givens(self):
        Qs=[]
        for COL in range(self.min):
            vi=self.R[:,COL]
            for ROW in range(COL+1,self.rows):
                if(vi[ROW]!=0):
                    GM=Ts.GivensMatrix(vi,ROW-1,ROW)
                    self.R=GM @ self.R
                    Qs.append(GM)
        self.Q=Qs[0].T
        for i in range(1,len(Qs)):
        	self.Q=self.Q@Qs[i].T

        return self.R,self.Q

"""
A=np.array([[6.0,5.0,0.0],[5.0,1.0,4.0],[0.0,4.0,3.0]])
#a=np.vstack([1.04,2.03,2.95,3.92,5.06,6.00,7.07])
#b = np.vstack([3.11,6.01,9.07,11.99,15.02,17.91,21.12])
#A=np.hstack((a,b))
A=np.array([[1.0,1.0],[0.0001,0.0],[0.0,0.0001]])

Fac=FactGivens(A)
R,Q=Fac.Givens()

print(R)
print(Q)
"""
