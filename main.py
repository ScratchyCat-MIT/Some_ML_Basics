import pandas as pd
from matplotlib import pyplot as plt
df = pd.read_csv('vgsales.csv')

X = df['NA_Sales'].values
y = df['Rank'].values

plt.scatter(X, y)
plt.show()