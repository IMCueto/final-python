from datetime import date
from datetime import datetime
#Día actual
today = date.today()
#Fecha actual
def fecha():
    return str(today)

hora_actual = datetime.now()

def minutos ():
    return hora_actual.minute
def segundos ():
    return hora_actual.second

m=minutos()
print(m)
#print(hora_actual.hour)
#print(hora_actual.minute)
#print(hora_actual.second)
#print(hora_actual.microsecond)