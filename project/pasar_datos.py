import pandas as pd
import sqlite3
from fecha import fecha


df=pd.read_csv('dataTienda.csv',sep=';')

def insertar_datos(w,x,y,z):
    conn=sqlite3.connect('tienda.db')
    cursor = conn.cursor()
    intruccion=f"INSERT  INTO VENTA VALUES ({w},{x},{y},{z})"
    cursor.execute(intruccion)
    conn.commit()
    conn.close()

print(df.head())
print (df.tail())
print(df.dtypes)
print(df.size)
print(df.describe())
print(df.columns)
columnsSelect = ['ORDER_ID','PRODUCT_ID','PRICE_TOTAL']
print(df[columnsSelect].head())
print(df['ORDER_ID'])
print(df.iterrows)

for i,fila in df.iterrows():
    a=fila['ORDER_ID']
    b=fila['PRODUCT_ID']
    c=fila['PRICE_TOTAL']
    insertar_datos(i+1,a,b,c)    
    if i+1==60:
        break
    print(i+1,a,b,c)
   
#venta=df[columnsSelect]
#print(venta.index)
#print(venta.loc[0])
#print('a')
#print(venta['PRICE_TOTAL'])