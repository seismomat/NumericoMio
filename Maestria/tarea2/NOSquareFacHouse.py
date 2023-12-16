import numpy as np
from numpy import linalg as LA
import Tools as Ts

"""
This program compute the QR factorization by HouseHolder method
and using an Rank complete matrix 
"""
class NOSquareFacHouse:
	def __init__(self,A):
		self.A=A
		self.n=self.A.shape[1]
		self.m=self.A.shape[0]
		self.min=np.minimum(self.n,self.m-1)
		self.R=np.copy(self.A)

	def HouseHolder(self):
		Qs=[]
		for i in range(self.min):
			ai=self.R[:,i][i:]
			ei=np.eye(ai.shape[0])[0]
			u=ai+Ts.sign(ai[0])*LA.norm(ai)*ei
			beta=1/(u.T@u)
			uu=u.reshape((ai.shape[0],1))
			uuT=u.reshape((1,ai.shape[0]))
			Haux=np.eye(ai.shape[0])-2*beta*(uu@uuT)
			H=Ts.Hfix(Haux,self.A)
			self.R=H @ self.R
			Qs.append(H)

		self.Q=Qs[0]
		for i in range(1,len(Qs)):
			self.Q=self.Q@Qs[i]

		return self.Q,self.R

"""
A=np.array([[1.0,1.0],[0.0001,0.0],[0.0,0.0001]])
A=np.array([[0,1,1],[1,2,3],[1,1,1]])

Fac=NOSquareFacHouse(A)
Q,R=Fac.HouseHolder()
print(Q)
print(R)
"""
