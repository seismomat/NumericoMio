import numpy as np

class Sust:
	def __init__(self,L,U,b):
		self.L=L
		self.U=U
		self.b=b
		self.sustDelante()
		self.sustAtras()

	def sustDelante(self):
		n=len(self.L)
		self.y=np.empty_like(self.b)
		self.y[0] = self.b[0]/self.L[0][0]
		for i in range(1,n):
			self.y[i] = self.b[i]
			for j in range(0,i):
				self.y[i] -= self.L[i][j]*self.y[j]
			self.y[i] /= self.L[i][i]

	def sustAtras(self):
		n=len(self.U)
		self.x=np.empty_like(self.y)
		self.x[n-1] = self.y[n-1]/self.U[n-1][n-1]
		for i in range(n-2,-1,-1):
			self.x[i] = self.y[i]
			for j in range(i+1,n):
				self.x[i] -= self.U[i][j]*self.x[j]
			self.x[i] /= self.U[i][i]

	def get_Solve(self):
		return self.x
