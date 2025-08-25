'''Add a column 'Average' = mean of Math, Science, English, Computer.'''

import pandas as pd 

df= pd.read_csv("students_performance.csv")

dfc=df.copy()

dfc['Average']=dfc[['Math', 'Science', 'English', 'Computer']].mean(axis=1)

print(dfc[['Student_ID','Average']].to_string(index=False))