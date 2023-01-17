import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np


df = pd.read_csv('Table21.csv')


X, y = df[['0','1','2']].values, df['3'].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=0)
model = LinearRegression().fit(X_train, y_train)

# aplikacja modelu na zbiorze testowym
predictions = model.predict(X_test)
print('Wartosci oszacowane przez model: ', np.round(predictions)[:10])
print('Wypożyczenia ze zbioru testowego   : ' ,y_test[:10])