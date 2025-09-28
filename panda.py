import pandas as pd 

df= pd.read_csv('students_performance.csv', index_col=0)


print(df[:5])