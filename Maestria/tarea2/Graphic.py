import matplotlib.pyplot as plt

class Graphic:
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
    for i in range(len(self.Fit[1])):
        plt.plot(self.Fit[0],self.Fit[1][i],label='Ajuste de grado'+str(self.info['grades'][i]))
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
    plt.plot(self.Data[0],self.Data[1],label='Datos',color='black',marker='o',linestyle=' ')
    for i in range(len(self.Res)):
        plt.plot(self.Fit[0],self.Res[i],label='Ajuste de grado'+str(self.info['grades'][i]),marker='*',linestyle=' ')
    plt.title('Residuales',fontsize=14)
    plt.grid()
    plt.xlabel(self.info['x'],fontsize=14)
    plt.xticks(fontsize=11)
    plt.ylabel(self.info['y'],fontsize=14)
    plt.yticks(fontsize=11)
    plt.legend()
    plt.show()

  def plotCond(self,dat):
    plt.figure(figsize=(9,6))
    plt.plot(dat[0],dat[1],color='black',marker='o',linestyle=' ')
    plt.title('Condicionamiento',fontsize=14)
    plt.grid()
    plt.xlabel('Órdenes del ajuste',fontsize=14)
    plt.xticks(fontsize=11)
    plt.ylabel('Números de condición',fontsize=14)
    plt.yticks(fontsize=11)
    if dat[2]=='yes':
        plt.yscale('log')
    plt.show()
