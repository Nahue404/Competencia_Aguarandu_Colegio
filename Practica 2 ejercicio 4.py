#El mayor número impar:
#Vamos a utilizar la función max(a,b) 
#Pide al usuario dos números par menor o más cercano, si es par halla el
#número impar mayor más cercano

N1=int(input("Ingrese el primer valor:"))
N2=int(input("Ingrese el segundo valor:"))

if (N1%2==0):
    NM=N1+1#Número mayor impar
    print("El número impar mayor más cercano es:",NM)
else:
    NM=N1-1#Número mayor par
    print("El número par mayor más cercano es:",NM)
if (N2%2==0):
    NM=N2+1#Número mayor impar
    print("El número impar mayor más cercano es:",NM)
else:
    NM=N2-1#Número mayor par
    print("El número par mayor más cercano es:",NM)

