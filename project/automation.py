import pywhatkit as pw
import requests
import pandas as pd
import os
import db
import sqlite3
from fecha import fecha,minutos,segundos
import xlwt
message="""
    1)Insertar data:
    2)Actualizar data del dolar
    3)Reciba ofertas y promociones en su wp
    0)Salir
"""
#print(message)
#a=int(input('ingrese la tarea a realizar: '))


def insertData():
    path_=os.getcwd()+'\dataTienda.csv'
    """
    #obtiene la ruta absoluta
    #conection a bd
    conn=db.Conection('tienda.db')
    cursor=conn.getCursor()
    print(path_)
    """
    df = pd. read_csv (path_, sep = ";") 
    ### logica para insertar 
    conn=sqlite3.connect('tienda.db')
    cursor = conn.cursor()
    ###crear un insertar para cada tabla
    selected_tabla = input("Seleccione la la categoria en la cual desea insertar su informacion:\n(PRODUCTOS | VENTAS | USUARIOS| INVENTARIO):\n")
    selected_tabla=selected_tabla.upper()
    if selected_tabla=="PRODUCTOS":
        #intruccion=f" SELECT ID FROM PRODUCTOS WHERE ID = (SELECT MAX(ID) FROM PRODUCTOS)"
        #cursor.execute(intruccion)
        #cont=cursor.fetchall()
        df=pd.read_sql("SELECT * FROM PRODUCTOS",conn)#para obtener el ultimo elemento y utilizarlo para insertar en la tabla
        a=df.at[df.index[-1],"ID"]
        print(a)
        b=input("Ingrese el nombre del producto:\n")
        c=float(input("Ingrese el precio del producto:\n"))
        d=input("Ingrese la categoria del producto:\n")
        e=int(input("Ingrese el stock actual del producto:\n"))
        f=fecha()
        intruccion=f"INSERT  INTO PRODUCTOS VALUES ({a+1},'{b}',{c},'{d}',{e},'{f}','{f}')"
        cursor.execute(intruccion)
        conn.commit()
        df=pd.read_sql("SELECT * FROM PRODUCTOS",conn)#para actualizar la tabla
        print(df.tail())#mostrar los ultimos 5 elementos
        df.to_excel('./reportes_generados/PRODUCTOS.xlsx',
            sheet_name='data',encoding='utf-8',index=False)
        print("Archivo .xlxx generado en reportes")
        os.system("pause")
        os.system("cls")
        #ya se agrego a la tabla
        #conn.commit()
        #conn.close()
        
        
    elif selected_tabla=='USUARIOS':
        df=pd.read_sql("SELECT * FROM USUARIOS",conn)#para obtener el ultimo elemento y utilizarlo para insertar en la tabla
        a=df.at[df.index[-1],"ID"]
        print(a)    
        b=input("Ingrese el nombre del Usuario:\n")
        c=input("Ingrese su contraseña:\n")
        d=input("Ingrese su correo electronico:\n")
        e=input("Ingrese su Apellido:\n")
        score=0
        tipoUsuario='PY_VAR4'
        intruccion=f"INSERT  INTO USUARIOS VALUES ({a+1},'{b}','{c}','{d}','{e}',{score},'{tipoUsuario}')"
        cursor.execute(intruccion)
        conn.commit()
        df=pd.read_sql("SELECT * FROM PRODUCTOS",conn)#para actualizar la tabla
        print(df.tail())#mostrar los ultimos 5 elementos
        df.to_excel('./reportes_generados/PRODUCTOS.xlsx',
            sheet_name='data',encoding='utf-8',index=False)
        print("Archivo .xlxx generado en reportes")
        os.system("pause")
        os.system("cls")
 
    elif selected_tabla=='INVENTARIO':
        df=pd.read_sql("SELECT * FROM INVENTARIO",conn)#para obtener el ultimo elemento y utilizarlo para insertar en la tabla
        a=df.at[df.index[-1],"ID"]
        print(a)    
        b=int(input("Ingrese el ID del producto:\n"))
        c=int(input("Ingrese la cantidad del producto"))
        f=fecha()
        intruccion=f"INSERT  INTO INVENTARIO VALUES ({a+1},{b},{c},'{f}')"
        cursor.execute(intruccion)
        conn.commit()
        df=pd.read_sql("SELECT * FROM PRODUCTOS",conn)#para actualizar la tabla
        print(df.tail())#mostrar los ultimos 5 elementos
        df.to_excel('./reportes_generados/INVENTARIO.xlsx',
            sheet_name='data',encoding='utf-8',index=False)
        print("Archivo .xlxx generado en reportes")
        os.system("pause")
        os.system("cls")
        #conn.close()
        
    elif selected_tabla=="VENTA":
        df=pd.read_sql("SELECT * FROM VENTA",conn)#para obtener el ultimo elemento y utilizarlo para insertar en la tabla
        a=df.at[df.index[-1],"ID"]
        print(a)    
        b=int(input("Ingrese el ID de la orden:\n"))
        c=int(input("Ingrese el ID del producto"))
        d=int(input("Ingrese el precio total del producto:\n"))
        intruccion=f"INSERT  INTO VENTA VALUES ({a+1},{b},{c},{d})"
        cursor.execute(intruccion)
        conn.commit()
        df=pd.read_sql("SELECT * FROM PRODUCTOS",conn)#para actualizar la tabla
        print(df.tail())#mostrar los ultimos 5 elementos
        df.to_excel('./reportes_generados/VENTA.xlsx',
            sheet_name='data',encoding='utf-8',index=False)
        print("Archivo .xlxx generado en reportes")
        os.system("pause")
        os.system("cls")
    
#   for i,fila in df.iterrows():
#       print(fila['ORDER_ID'])

def updateDolar():
    url = 'https://api.apis.net.pe/v1/tipo-cambio-sunat' #tipo cambio sunat
    response=requests.get(url)
    data=response.json()  
#    for i in data:
#       print (i)
#    print(data.keys())
#    print(data.values())
    compra=data['compra']
    venta=data['venta']
    fecha_dolar=data['fecha']
    conn=sqlite3.connect('tienda.db')
    cursor = conn.cursor()
    df=pd.read_sql("SELECT * FROM TASA_CAMBIOS",conn)
    a=df.at[df.index[-1],"ID"]
    msg="""
    ---------------------------------------
                DOLAR PRECIOS
    ---------------------------------------
    """
    print(msg)
    print("COMPRA => ",compra)
    print("VENTA => ",venta)
    print("FECHA => ",fecha_dolar)
    os.system("pause")
    os.system("cls")
    intruccion=f"INSERT  INTO TASA_CAMBIOS VALUES ({a+1},{compra},{venta},'{fecha_dolar}')"
    cursor.execute(intruccion)
    conn.commit()
    df=pd.read_sql("SELECT * FROM TASA_CAMBIOS",conn)#para actualizar la tabla
    print(df.tail())#mostrar los ultimos 5 elementos
    df.to_excel('./reportes_generados/PRECIO_DOLAR.xlsx',
    sheet_name='data',encoding='utf-8',index=False)
    print("Archivo .xlxx generado en reportes")
    os.system("pause")
    os.system("cls")

def promocion():
    promocion_msg="""
    *Gracias por elegirnos como su tienda de preferencia:*
    Por la compra de 3 productos o mas llevese gratis entradas para\n
    la pelicula que quiera, valida solo en establecimientos anticine
    """
    numero=int (input("Ingrese su numero de telefono"))
    m=minutos()
    m+=1
    s=segundos
    pw.sendwhatmsg(numero,promocion_msg,m,s)
    print("mensaje enviado\n")
    os.system("pause")
    os.system("cls") 

opcion=1
while(opcion):
    print(message)
    opcion=int(input("Seleccione una opcion:\n"))
    if opcion==1:
        insertData()
    elif opcion==2:
        updateDolar()
    elif opcion==3:
        promocion()
    elif opcion==0:
        print("gracias")
