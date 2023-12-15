#Escribir una funcion que calcule el total de una factura tras aplicarle el IVA. 
#La funcion debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, 
#y devovler el total de la factura. Si se invoca la función sin pasarle el porcentaje de IVA, 
#debera aplicar un 21%.
def Factura(Monto,PorcentajedeIVA=0.21):
	return (Monto-(Monto*PorcentajedeIVA))

IVA=int(input("Ingrese 1 si quieres agregar el porcentaje del IVA o 2 si quieres que su porcentaje sea 21%:"))
if IVA == 1:
	Monto=int(input("Escribe la cantidad sin IVA:"))
	print("Ejemplo: El porcentaje es 0.50 ")
	PorcentajedeIVA=float(input("Escribe el IVA con 0 y coma(,):"))

	print(Factura(Monto,PorcentajedeIVA))
else:
	print(Factura((int(input("Ingrese cantidad sin IVA:")))))