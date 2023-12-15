#Imagina que pides al usuario que piense en un número de cinco
#dígitos, luego sigue los pasos
print("Piense en un número de 6 digitos")
Primerosnumeros=int(input("Ingrese los primeros 3 números:"))#Los primeros 3 números pensado
Ejer1= ((Primerosnumeros*80)+1)*250#la variable donde se va a resolver todos los valores
Segundosnumeros=int(input("Ingrese los ultimos números:"))#Los ultimos 4 números pensado
Ejer1 += Segundosnumeros
Ejer1 += Segundosnumeros
Ejer1 -=250
Ejer1 =Ejer1/2
int(Ejer1)
print(Ejer1)
