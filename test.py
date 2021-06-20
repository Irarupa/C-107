import pandas as pd
import plotly.graph_objects as go
import statistics

test_read = pd.read_csv('data.csv')
test_score = test_read.loc[test_read['student_id']=='TRL_xsl']
print(test_read.head())
print(test_score.groupby('level')['attempt'].mean())

fig = go.Figure(go.Scatter(x = test_score.groupby('level')['attempt'].mean() , y = ['level1','level2','level3','level4']),color = 'attempt')
