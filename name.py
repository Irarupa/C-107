import  pandas as pd
import plotly.graph_objects as go
import statistics as stat

stud_read = pd.read_csv('data.csv')
print(stud_read.groupby('level')['attempt'].mean())

fig = go.Figure(go.Bar(y = ['level1','level2','level3','level4'],x = stud_read.groupby('level')['attempt'].mean(),orientation = 'h', color= 'attempt'))

fig.show()