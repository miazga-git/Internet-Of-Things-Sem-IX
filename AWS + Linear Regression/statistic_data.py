import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('Table21.csv')

print('Srednia wartosc wynosi: '+ str(df['1'].mean()))
print('Odchylenie standardowe wynosi: ' + str(df['1'].std()) )