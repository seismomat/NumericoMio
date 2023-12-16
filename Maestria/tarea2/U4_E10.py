import numpy as np
import LinearRegresssion as LR
import matplotlib.pyplot as plt

t= np.arange(20,46,dtype='float64')
y=[431.0,409.0,429.0,422.0,530.0,505.0,459.0,499.0,526.0,563.0,587.0,595.0,
647.0,669.0,746.0,760.0,778.0,828.0,846.0,836.0,916.0,956.0,1014.0,1076.0,1134.0,1024.0]

settings={'titulo':'Regresión lineal con ecuaciones normales',
'x':'Tiempo [seg]','y': 'Valores del experimento','grades':1}
information={"Functions":'basics',"weight":'null'}

datas={'information':information,'y':y,'t':t,'settings':settings}

Res,y_g=LR.LinearRegressionS(datas)

t20_28=t[:9];y20_28=y[:len(t[:9])];
t28_39=t[8:20]; y28_39=y[8:20]
t39_45=t[19:];y39_45=y[19:]


datas={'information':information,'y':y20_28,'t':t20_28,'settings':settings}
Res20_28,y_g20_28=LR.LinearRegressionS(datas)

datas={'information':information,'y':y28_39,'t':t28_39,'settings':settings}
Res28_39,y_g28_39=LR.LinearRegressionS(datas)

datas={'information':information,'y':y39_45,'t':t39_45,'settings':settings}
Res39_45,y_g39_45=LR.LinearRegressionS(datas)




plt.plot(t20_28,y_g20_28,label='aproximación en [20,28]')
plt.plot(t28_39,y_g28_39,label='aproximación en [20,28]')
plt.plot(t39_45,y_g39_45,label='aproximación en [20,28]')
plt.plot(t,y_g,color='black',label='aproximación lineal completa')
plt.plot(t,y,marker='o',linestyle='',color='blue')
plt.xlabel("Edades")
plt.ylabel("Tasa de mortalidad")
plt.grid()
plt.legend()
plt.show()

information={"Functions":'l2',"weight":'null'}
datas={'information':information,'y':y20_28,'t':t20_28,'settings':settings}
Res20_28,y_g20_28=LR.LinearRegressionS(datas)
information={"Functions":'l2',"weight":'null'}
datas={'information':information,'y':y28_39,'t':t28_39,'settings':settings}
Res28_39,y_g28_39=LR.LinearRegressionS(datas)
information={"Functions":'l4',"weight":'null'}
datas={'information':information,'y':y39_45,'t':t39_45,'settings':settings}
Res39_45,y_g39_45=LR.LinearRegressionS(datas)

plt.plot(t20_28,y_g20_28/(6.5),label='aproximación en [20,28]')
plt.plot(t28_39,y_g28_39/(-15),label='aproximación en [20,28]')
plt.plot(t39_45,y_g39_45/(11.5),label='aproximación en [20,28]')
plt.plot(t,y,marker='o',linestyle='',color='blue')
plt.xlabel("Edades")
plt.ylabel("Tasa de mortalidad")
plt.grid()
plt.legend()
plt.show()
