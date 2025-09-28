import pandas as pd 
df=pd.read_excel("Customer Call List.xlsx")

df['Phone_Number'] = df['Phone_Number'].astype(str)
df['Phone_Number']=df['Phone_Number'].str.replace('[^0-9]','',regex=True)
df['Phone_Number']=df['Phone_Number'].apply(lambda x: x[0:3]+'-'+ x[3:6]+'-'+x[6:10])
# df['Phone_Number']=df['Phone_Number'].apply(lambda x: str(x))

print(df['Phone_Number'])