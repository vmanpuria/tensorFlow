import pandas as pd
import numpy as np

df=pd.read_csv("topic.txt", header=None, names=["keyword"])
keys=df['keyword'].unique()
for key in keys:
  print(key)
print('Total keys:', keys.size)
