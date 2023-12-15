#Números Iguales
#Dados tres números, determina cúantos de ellos son iguales:

N1=int(input("Ingresa su primer número:"))
N2=int(input("Ingresa su segundo número:"))
N3=int(input("Ingresa su tercer número:"))

if(N1!=N2 and N1!=N3 and N2!=N3):
    print("Ningunos son iguales")
elif(N1==N2 and N1==N3 and N2==N3):
    print("Tres son iguales")
else:
    print("Dos son iguales")

