'''Show basic info (rows, columns) and first 5 rows.'''
import pandas as pd 

df=pd.read_csv('students_performance.csv')

print(df.shape)

print(df.head())