import csv
import plotly.graph_objects as rasengan
import plotly_express as ass
import random
rasenkyugan = []
count = []
for i in range(0,1000):

    rasenshuriken1 = random.randint(1,6)
    rasenshuriken2  = random.randint(1,6)
    rasenkyugan.append(rasenshuriken1 + rasenshuriken2)
    count.append(i)

fig = ass.bar(x= rasenkyugan, y = count)
fig.show()