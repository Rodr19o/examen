
import os
import random
import csv
import time
import msvcrt
cleanse=lambda: os.system("cls")
trabajadores = ["Juan Perez","Maria Garcia","Carlos Lopez","Ana Martinez","Pedro Rodriguez","Laura Hernandez","Miguel Sanchez","Isabel Gomez","Francisco Diaz","Elena Fernandez"]
empleados=[]
def menu():
    while True:
        try:
            cleanse()
            print("----------Menu----------\n")
            print("""1.Asignar sueldos aleatoriamente
2.Clasificar sueldos
3.Reporte de sueldos
4.Estadisticas
5.Salir del programa
""")
            print("-------------------------")

            colocolo=int(input("Opcion: "))
            if colocolo in [1,2,4,5]:
                return colocolo
            if colocolo==3:               
                reporte()
                print("Csv creado")
                msvcrt.getch()               
        except ValueError:
            print("Error")
            time.sleep(1)
def asignar_sueldos():
    global empleados
    empleados=[]
    for dicc in trabajadores:
        person={}
        sueldo=random.randint(300000,2500000)
        person={"Nombre":dicc,"Sueldo":sueldo,"Desc.Salud":int(sueldo*0.07),"Desc.Afp":int(sueldo*0.12),"Desc.Liquid":int(sueldo*0.81)}
        empleados.append(person)

def reporte():
    with open("Reporte.csv","w",newline="") as archivo:
        escritor=csv.writer(archivo)
        escritor.writerow(["Nombre empleado","Sueldo Base","Descuento Salud","Descuento AFP","Sueldo Liquido"])
        for dicc in empleados:
            escritor.writerow([dicc["Nombre"],dicc["Sueldo"],dicc["Desc.Salud"],dicc["Desc.Afp"],dicc["Desc.Liquid"]])

def estadisticas():
    if not empleados:
        asignar_sueldos()
    larga=max(empleados,key=lambda x: x["Sueldo"])
    corta=min(empleados,key=lambda x: x["Sueldo"])
    print(f"El que gana mas es {larga["Nombre"]} con un sueldo de ${larga["Sueldo"]:,}")
    print(f"El que gana menos es {corta["Nombre"]} con un sueldo de ${corta["Sueldo"]:,}")
    total2=sum(dicc["Sueldo"] for dicc in empleados)
    total2=int(total2/10)
    print(f"El promedio de sueldos es de ${total2:,}")
    
def clasificar():
    total=0
    menor=[i for i in empleados if i["Sueldo"]<=800000]
    mitad=[i for i in empleados if i["Sueldo"]>800000 and i["Sueldo"]<=2000000]
    mayor=[i for i in empleados if i["Sueldo"]>2000000]
    print(f"Sueldos menores a $800000 TOTAL: {len(menor)}")
    print("Nombre\t\tSueldo")
    for dicc in menor:
        print(f"{dicc["Nombre"]}\t${dicc["Sueldo"]:,}")
    print(f"Sueldos entre $800000 y $2000000 Total:{len(mitad)}")
    print("Nombre\t\tSueldo")
    for dicc in mitad:
        print(f"{dicc["Nombre"]}\t${dicc["Sueldo"]:,}")
    print(f"Sueldos superiores a $2000000 TOTAL{len(mayor)}")
    print("Nombre\t\tSueldo")
    for dicc in mayor:
        print(f"{dicc["Nombre"]}\t${dicc["Sueldo"]:,}")
    for dicc in empleados:
        total+=dicc["Sueldo"]
    print(f"TOTAL SUELDOS: ${total:,}")
while True:
    principal=menu()
    if principal==1:
        asignar_sueldos()
        print("Sueldos asignados")
        msvcrt.getch()
    elif principal==2:
        cleanse()
        clasificar()
        msvcrt.getch()
    elif principal==4:
        cleanse()
        estadisticas()
        msvcrt.getch()
    else:
        cleanse()
        print("Finalizando programa...")      
        print("Desarrollado por Calfiqueo Rodrigo")
        print("20.395.871-4")
        print("...")
        time.sleep(3)
        break