import datetime
dia = int(input("Dia : "))
mes = int(input("Mes : "))
anio = int(input("Año : "))
fecha = datetime.datetime(anio, mes, dia)
if mes < 9:
    primavera = datetime.datetime(anio, 9, 21)
elif mes == 9 and dia < 21:
    primavera = datetime.datetime(anio, 9, 21)
else:
    primavera = datetime.datetime(anio+1, 9, 21)
diferencia = primavera-fecha
print(f" Faltan {diferencia.days} dias para la primavera")