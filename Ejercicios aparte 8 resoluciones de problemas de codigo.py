def coordenadasZ(x,y):
    X= x+10
    y=y+15
    return x+y
    
#Programa principal 
x= int(input("Coordenada eje x: "))
y= int(input("Coordenada eje y: "))
for i in range(3):
    z=coordenadasZ(x,y)
    X=x+1
    y=y+1
print(x," . ",y)
