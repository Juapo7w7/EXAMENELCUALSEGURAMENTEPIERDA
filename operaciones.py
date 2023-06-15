#Debe de realizar un algoritmo el cual resuelva los siguientes problemas de
#matemática:
# Suma (+)
# Resta (-)
# Multiplicación (*)
# División (/)
# Exponenciación (**)
# Raíces (Función sqrt() de la librería math)
# Suma de 5 números
# Residuo (%)
# Quetzal (Q7.91) a Dólar ($1)
# Dólar ($1) a Quetzal (Q7.91)
import math

def suma (a,b):
    resultado= a+b
    return resultado

def resta (a,b):
    return a-b

def multiplicacion (a,b):
    return a*b

def division (a,b):
    return a/b 

def exponenciacion (a,b):
    return a**b

def raizcuadrada (a):
    return math.sqrt(a)

def sumadecinco (a,b,c,d,e):
    return a+b+c+d+e

def residuo (a,b):
    return a%b

def QaD (a,b):
    return a/b

def DaQ (a,b):
    return a*b