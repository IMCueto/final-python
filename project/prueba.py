import pandas as pd
import sqlite3
sq=sqlite3.connect('tienda.db')
df=pd.read_sql("SELECT * FROM PRODUCTOS",sq)
print(df.head())
print(df.tail(1))
print(df['ID'].tail(1))
a=df['ID'].tail(1)
print(df['ID'])
print(df[-1:])
print("\n\n")

print(df.at[df.index[-1], "ID"])
#para obtener el ultimo valor 


#df["ID"][-1:]
#df["ID"].iat[-1]
#df.iat[-1, df.columns.get_loc("ID")]