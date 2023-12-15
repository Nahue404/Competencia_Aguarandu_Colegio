#Crea un programa en Python para dibujar un triangulo 
#como el siguiente:
#*
#**
#***
#****
#*****
#****
#***
#**
#*
for a in range(5):
    for e in range(a+1):
        print("*",end=" ")
    print("\n")

for a in range(5,1,-1):
    for e in range(a-1):
        print("*", end=" ")
    print("\n")
