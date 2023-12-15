#2. Leer números enteros de teclado, hasta que el usuario ingrese el 0.
#Finalmente, mostrar la sumatoria de todos los números positivos ingresados.
num= 1 
cont= 0
while num != 0:
    num= int(input("Ingrese un número entero o ingrese 0 para terminar de jugar:"))
    if num > 0:
        cont+=num
if num == 0:
    cont-1
    print("La suma de los valores ingresados es:" ,cont)
