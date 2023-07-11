import numpy as np
import os
def llenarcasa(casa):
    p=1
    for i in range(10):
        for j in range(4):
            casa[i,j]=p
            p+=1
def validaop(op):
    while(True):
        try:
            op=int(input(" Elija Una opción "))
            if(op>=1 and op<=5):
                break
            else:
                print("Debe escoger una opción valida 1/2/3/4/5")
        except ValueError:
            print("Debe ser un número entero")

def mostrardisponible(casa):
    os.system("cls")
    for i in range(10):
        for j in range(4):
            if(j==1):
                print(casa[i,j])
            else:
                print(casa[i,j])
def validacasa(val):
    casa=0
    while(True):
        try:
            casa=int(input("Ingrese número de departamento 1 - 40 "))
            if(casa>=1 and casa<=40):
                break
            else:
                print(" Error debe ingresar una opción valida")
        except ValueError:
            print(" Error, Ingrese una opción valida")
    return val 

def buscardisponible(casa,val):
    for i in range(10):
        for j in range(4):
            if(val==casa[i,j]):
                return True
    return False

def comprarcasa(casa,val,ruts):
    for i in range(10):
        for j in range(4):
            if (casa[i,j]==val):
                casa[i,j]="X"
                if j==0:
                    pago=3800
                if j==1:
                    pago=3000
                if(j==2):
                    pago=2800
                if(j==3):
                    pago=3500
            while(True):
                while(True):
                    try:
                        rut=int(input("Ingrese su rut sin puntos ni guion (minimo 8 digitos"))
                        if(rut<9999999):
                            print("Error, debe tener minimo 8 digitos")
                        else:
                            break
                    except ValueError:
                        print("El rut no debe contener puntos ni guion, y debe ser un numero")
                if(len(ruts)>0):
                    sw=0
                    for y in range(len(ruts)):
                        if(rut==ruts[y]):
                            sw=1
                    if(sw==1):
                        print("El rut ya existe ")
                    else:
                        ruts.append(rut)
                        break
                else:
                    ruts.append(rut)
                    break
    return pago

def listado(r):
    r.sort()
    print("Listado de compradores por rut ordenados de menor a mayor")
    print("\t",r)
