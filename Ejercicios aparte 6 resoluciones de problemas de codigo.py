def maximo(a,b):
    if x>y:
        return x-3
    else:
        return y+1

def minimo(a,b):
    if x<y:
        return y+1
    else:
        return x-3

#programa principal
x= int(input("Un número: "))
y= int(input("Otro número: "))
print(maximo(x-3,y+2), minimo (x+2, y-3))
