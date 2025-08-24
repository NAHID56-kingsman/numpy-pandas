''' Question : From df['Math'] as NumPy array, compute mean, std (ddof=1), min, max, argmax index.
'''
import numpy as np
import pandas as pd

df=pd.read_csv("students_performance.csv")

arr=df['Math'].to_numpy()

print(arr)

print('MEAN',arr.mean())  #print(np.mean(arr)) same

print('MAX',arr.max())

print('MIN',arr.min())

print('ARGMAX',arr.argmax())

print('STD',np.std(arr,ddof=1)) #Population Std ddof=0 //Sample Std=1

