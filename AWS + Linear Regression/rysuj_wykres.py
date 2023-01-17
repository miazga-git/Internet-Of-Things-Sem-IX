import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('Table21.csv')

df.plot(kind='line', x='4', y='1')

plt.show()
