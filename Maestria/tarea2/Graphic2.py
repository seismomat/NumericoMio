import matplotlib.pyplot as plt

class Graphic2:
  def __init__(self,info):
    self.info=info['settings']
    self.Data=info['Data']
    self.Fit=info['Fit']
    self.Res=info['Res']
    self.plott()
    self.plotRes()

  def plott(self):
    plt.figure(figsize=(9,6))
    plt.plot(self.Data[0],self.Data[1],label='Datos',color='black',marker='o',linestyle=' ')
    plt.plot(self.Fit[0],self.Fit[1],label='Ajuste de grado lineal',color='red')
    plt.title(self.info['titulo'],fontsize=14)
    plt.grid()
    plt.xlabel(self.info['x'],fontsize=14)
    plt.xticks(fontsize=11)
    plt.ylabel(self.info['y'],fontsize=14)
    plt.yticks(fontsize=11)
    plt.legend()
    plt.show()

  def plotRes(self):
    plt.figure(figsize=(9,6))
    plt.plot(self.Fit[0],self.Res,color='black',marker='*',linestyle=' ')
    plt.title('Residuales',fontsize=14)
    plt.grid()
    plt.xlabel(self.info['x'],fontsize=14)
    plt.xticks(fontsize=11)
    plt.ylabel(self.info['y'],fontsize=14)
    plt.yticks(fontsize=11)
    plt.show()
