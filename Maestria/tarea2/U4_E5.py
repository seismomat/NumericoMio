import numpy as np
from numpy import linalg as LA
import Normals as Ns
import Graphic2 as Gr
import Tools as Ts

import LinearRegresssion as LR

y=[5.0291,6.5009,5.3666,4.1272,4.2948,6.1261,12.5140,10.0502,9.1614
,7.5677,7.2920,10.0357,11.0708,13.4045,12.8415,11.9666,11.0765,11.7774,14.5701
,17.0440,17.0398,15.9069,15.4850,15.5112,17.6572]
t=np.arange(1,26,dtype='float64')

settings={'titulo':'Regresión lineal con ecuaciones normales',
'x':'Tiempo [seg]','y': 'Valores del experimento','grades':1}
information={"Functions":'basics',"weight":'null'}

datas={'information':information,'y':y,'t':t,'settings':settings}

Res=LR.LinearRegression(datas)

###
y=np.array(y)
Res=np.array(Res)
y=y[Res<3]
t=t[Res<3]

datas={'information':information,'y':y,'t':t,'settings':settings}
Res=LR.LinearRegression(datas)

Res=LR.LinearRegression1(datas)
