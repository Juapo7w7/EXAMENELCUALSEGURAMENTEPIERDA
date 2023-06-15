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

elif tipooperacion==3:
    from operaciones import multiplicacion
    a=(int(input("Ingrese un primer numero ")))
    b=(int(input("Ingrese el numero por lo cual quiere multiplicarlo  ")))
    totalmultiplicacion= multiplicacion(a,b)
    print (totalmultiplicacion)

elif tipooperacion==4:
    from operaciones import division
    a=(int(input("Ingrese el numero el cual desea dividar  ")))
    b=(int(input("Ingrese el numero por el cual desea dividirlo ")))
    totaldision= division(a,b)
    print (totaldision)

elif tipooperacion==5:
    from operaciones import exponenciacion
    a=(int(input("Ingrese un numero  ")))
    b=(int(input("Ingrese el numero ppor el cual lo quiere elevar  ")))
    totalexpo= exponenciacion(a,b)
    print (totalexpo)

elif tipooperacion==6:
    from operaciones import raizcuadrada
    a=(int(input("Ingrese el numero al cual le quiera sacar la raiz  ")))
    totalraiz= raizcuadrada(a)
    print (totalraiz)


elif tipooperacion==7:
    from operaciones import sumadecinco
    a=(int(input("Ingrese un numero  ")))
    b=(int(input("otro un numero  ")))
    c=(int(input("otro un numero  ")))
    d=(int(input("otro un numero  ")))
    e=(int(input("otro un numero  ")))
    total5= sumadecinco(a,b,c,d,e)
    print (total5)
