#Promedios de n números
#Pide al usuario que ingrese números al azar,
#o que ingrese 0 para terminar de ingresar números
#Luego halla el promedio de los números ingresados y
#escribe el enunciado en la pantalla
NA=1
Sum=0
Con=0

while NA != 0:
    NA=int(input("Ingrese un número al azar o ingrese 0 para dejar de ingresar números:"))
    Sum= NA+Sum
    Con+=1
else:
    print("El promedio de los números ingresados es:",(Sum/Con-1) )
