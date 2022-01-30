import csv
import plotly_express as ass
import pandas as pp
import plotly.figure_factory as fussy
df = pp.read_csv("bellcurve2.csv")
fig = fussy.create_distplot([df["Avg Rating"].tolist()], ["Avg Rating"])
fig.show()
