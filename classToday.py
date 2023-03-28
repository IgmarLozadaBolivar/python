""" fecha = input("Ingrese una fecha dd/mm/aaaa: ")
day = int(fecha[0:2])
moth = int(fecha[3:5])
year = int(fecha[6:10])
feb = 0
days = 0

if year % 4 == 0 and (year % 400 == 0 or year % 100 != 0):
    feb = 29
else:
    feb = 28

dayMoth = [31, feb, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for i in range(moth - 1):
    days += dayMoth[i]
days += day
print(fecha, 'es el', days, 'del año', year) """
