import tabula as tb
import pandas as pd
import re

file = '/home/mating/Downloads/tarea_unidades4y5_2021-2.pdf'

#data = tb.read_pdf(file, area = (300, 0, 600, 800), pages = '1')
#print(data)

from tika import parser
raw = parser.from_file(file)
tika_text = raw['content'].split()

data=tika_text[145:189]

for i in range(len(data)):
    data[i]=data[i].replace(',',' ')
    data[i]=data[i].replace('[',' ')
    data[i]=data[i].replace(']',' ')

t=data[2:22]
y=data[24:49]

for i in range(len(t)):
    t[i]=float(t[i])
    y[i]=float(y[i])


t2=tika_text[302:327]
for i in range(len(t2)):
    t2[i]=t2[i].replace(',',' ')
    t2[i]=float(t2[i])


x=tika_text[785:806][:10]
y=tika_text[785:806][11:]

for i in range(len(x)):
    x[i]=float(x[i])
    y[i]=float(y[i])
