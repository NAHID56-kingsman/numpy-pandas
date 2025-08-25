'''Use np.where to label Attendance_% >= 90 as 'Excellent', 75-89 as
'Good', else
'Needs-Work' for first 10 students.'''

import numpy as np 
import pandas as pd 

df=pd.read_csv('students_performance.csv')

arr=df['Attendance_%'].to_numpy()

detail=np.where (arr>=90,'Excelent',np.where(arr>=75,'Good','Needs-Work')) 

print(detail[:10])