import pandas as pd
from matplotlib import pyplot as plt
df = pd.read_csv('vgsales.csv')

X = df['NA_Sales']
y = df['Rank']

plt.scatter(X, y)