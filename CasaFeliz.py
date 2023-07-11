import numpy as np 
import Funciones as fn
import os
casa=np.empty([10,4],type(int))
fn.llenarcasa(casa)
os.system("cls")
op=0
casa1=0
while(op!=5):
    os.system("cls")
    print("********** Casa Feliz **********")
    print("================================")
    print(" 1. Comprar departamento")
    print(" 2. Mostrar departamentos disponibles")
    print(" 3. Ver listado de compradores")
    print(" 4. Mostrar ganacias totales")
    print(" 5. Salir ")
    op=fn.validaop(op)
    if(op==1):
        fn.mostrardisponible(casa)
        val=fn.validacasa(val)
        disponible=fn.buscardisponible(casa,val)
        if(disponible):
            print("Departamento disponible")
            pagar=fn.comprarcasa(casa,val,ruts)
            print("Usted debe cancelar un total de ",pagar)
            os.system("pause")
    if(op==2):
        fn.mostrardisponible(casa)
        os.system("pause")
    if(op==3):
        fn.listado(ruts)
        os.system("pause")
    if(op==4):

    if(op==5):
        print(" David Navarro 11/07/2023")
