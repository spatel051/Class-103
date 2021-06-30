import pandas as pd
import plotly.express as px

df = pd.read_csv('csv-files/data.csv')
fig = px.scatter(df, x = 'Population', y = 'Per capita', color = 'Country', title = 'Population', size = 'Percentage', size_max = 60)
fig.show()