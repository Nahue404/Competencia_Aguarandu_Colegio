#1.Clasificador de Números
#Pide un número al usuario, si es positivo imprime 1, si es negativo -1
#Y si 0 si es igual a 0

N=int(input("Ingrese un número:"))#Var. de Número

if N >= 0:
    print("1")
elif N<0:
    print("-1")
else:
    print("0")
