print ("Cual de las siguientes operaciones Desea ultilizar ")
print ("1.Suma ")
print ("2. Resta")
print ("3. Multiplicacion ")
print ("4. Division")
print ("5. Exponenciacion")
print ("6. Raiz Caudrada ")
print ("7. Suma de Cinco de cinco digitos ")
print ("8. Residuo ")
print ("9. Pasar Quetzales a Dolares ")
print ("10. Pasar Dolares a Quetzsales ")
tipooperacion=(int(input("Ingrese el numero de operacion que desea realizar ")))
if tipooperacion==1:
    from operaciones import suma
    a=(int(input("Ingrese un primer numero ")))
    b=(int (input("Ingrese otro numero "))) 
    totalsuma= suma(a,b)
    print (totalsuma)

elif tipooperacion==2:
    from operaciones import resta
    a=(int(input("Ingrese un primer numero ")))
    b=(int(input("Ingrese el numero por lo cual quiere restarlo ")))
    totalresta= resta(a,b)
    print (totalresta)





