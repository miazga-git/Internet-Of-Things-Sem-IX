
from random import randrange
import pandas as pd
import time
from datetime import datetime

table = []
df = pd.read_csv("Table21.csv")

for i in range(40):
    x = randrange(100)
    y = randrange(100)
    z = randrange(100)
    sum = x+y+z
    now = datetime.now()
    time.sleep(0.5)
    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)
    table.append([x,y,z,sum,current_time])
    dataframe = pd.DataFrame(table)
    dataframe.to_csv('Table21.csv', index=False)