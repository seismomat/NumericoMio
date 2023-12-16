import tabula as tb
import pandas as pd
import re

file = '/home/mating/Downloads/tarea_unidades4y5_2021-2.pdf'

#data = tb.read_pdf(file, area = (300, 0, 600, 800), pages = '1')
#print(data)

from tika import parser
raw = parser.from_file(file)
tika_text = raw['content']#.split()

m=re.findall("t[ =:]",tika_text)

m=re.search(m[2],tika_text)
print(m.span())
print(tika_text[m.span()[0]:m.span()[1]+10])
