'''Use broadcasting to standardize Math and Science (z-score). Return first
5 rows.'''

import numpy as np 
import pandas as pd

df=pd.read_csv('students_performance.csv')

arr=df[['Math','Science']].to_numpy()

mean=np.mean(arr,axis=0)  #axis=1 Row-wise // and axis=0 column-wise 
std=np.std(arr,axis=0,ddof=0)                          #population std #Population Std ddof=0 //Sample Std=1
z_scores = (arr - mean) / std

print(z_scores[:5])                          # z_scores = (arr - mean) / std