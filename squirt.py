import csv
import plotly_express as ass
import pandas as pp
import plotly.figure_factory as fussy
df = pp.read_csv("Bellcurve.csv")
fig  = fussy.create_distplot([df["Height(Inches)"].tolist()],["Height"],show_hist= False)
fig.show()


