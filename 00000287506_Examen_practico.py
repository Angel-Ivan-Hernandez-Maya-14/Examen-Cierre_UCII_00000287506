conta=0
contr=0
riesgorep=0
acumprom=0
promedios=[]
estudiantes={}

try:
    with open ("estudiantes.txt","r") as archivo:
        numid1=0
        for linea in archivo:
            if "Número de identificación del estudiante" in linea:
                numid1=int(linea.split(": ")[1].strip())
            elif "Nombre del estudiante" in linea:
                estudiantes[numid1]=linea.split(": ")[1].strip()
            elif "Promedio" in linea:
                prom=float(linea.split(": ")[1].strip())
                promedios.append(prom)
                acumprom+=prom
            elif "Situación: Aprobado" in linea:
                conta+=1
            elif "Situación: Riesgo" in linea:
                conta+=1
                riesgorep+=1
            elif "Situación: Reprobado" in linea:
                contr+=1
except FileNotFoundError:
    pass

def menu():
    print("\n================MENU DE OPCIONES===============\n")
    print("1. Registrar un estudiante")
    print("2. Mostrar todos los estudiantes registrados")
    print("3. Consultar el promedio de un estudiante")
    print("4. Mostrar estadísticas generales del grupo")
    print("5. Salir del programa\n")

def registrar(est,califs,conta,contr,riesgorep,acumprom):
    prom=sum(califs)/3
    if prom>=80 and prom<=100:
        sit="Aprobado"
        conta+=1
    elif prom>=70 and prom <80:
        sit="Riesgo de reprobación. Pero está aprobado"
        conta+=1
        riesgorep+=1
    else:
        sit="Reprobado"
        contr+=1
    promedios.append(prom)
    acumprom+=prom

    with open("estudiantes.txt","a") as archivo: 
        archivo.write(f"Número de identificación del estudiante: {list(est.keys())[-1]}\nNombre del estudiante: {list(est.values())[-1]}\nPrimera calificación: {califs[0]}\nSegunda calificación: {califs[1]}\nTercera calificación: {califs[2]}\nPromedio: {prom}\nSituación: {sit}\n================================================\n")
    return conta,contr,riesgorep,acumprom

def mostrar():
    print("\n========LISTA DE ESTUDIANTES REGISTRADOS========")
    with open("estudiantes.txt","r") as archivo:
        for linea in archivo:
            print(linea.strip())

def consultar():
    condicionb=False
    while condicionb==False:
        buscador=input("Ingrese el número de identificación del estudiante que desea consultar: ")
        if buscador.strip()=="":
            print("\nError: No debe de estar vacío. Intentelo de nuevo. ")
        else:
            condicionb=True
    encontrado=False
    try:
        print()
        with open("estudiantes.txt","r") as archivo:
            for linea in archivo:
                if linea.strip()==f"Número de identificación del estudiante: {buscador.strip()}":
                    encontrado=True
                elif encontrado==True:
                    if "Nombre del estudiante:" in linea or "Promedio:" in linea or "Situación:" in linea:
                        print(linea.strip())
                    if "Situación:" in linea:
                        break
        if encontrado==False:
            print("No se encontró ningún estudiante con ese número de idenificación :(")
    except FileNotFoundError:
        print("No hay estudiantes registrados.")
        print("Necesitas registrar al menos un estudiante.")

def estadisticas(dictestu):
    esreg=len(dictestu)
    if esreg>0:
        promg=sum(promedios)/esreg
        alto=max(promedios)
        with open("estadisticas.txt","w") as archivo:
                archivo.write(f"Estudiantes registrados: {esreg}\nPromedio general: {promg}\nAprobados: {conta}\nEn riesgo de reprobación: {riesgorep}\nReprobados: {contr}\nPromedio mas alto: {alto}")

        print("\n=====ESTADISTICAS DEL GRUPO=====")
        with open("estadisticas.txt","r") as archivo:
            for linea in archivo:
                print(linea.strip())
        print("================================")
    else:
        print("Todavía no hay estudiantes registrados.")    

print("\n=====SISTEMA DE REGISTRO Y ANÁLISIS DE ESTUDIANTES=====")
print("Sea bienvenido :)")
print("A continuación se mostrará el menú de las opciones que puede hacer en el sistema")
print("En caso de que la opción no sea válida, se volverá a mostrar el menú hasta que la opción sea válida")

while True:
    menu()
    opcion=int(input("¿Qué acción desea realizar? "))
    if opcion==1:
        condicionid=False
        while condicionid==False:
            numid=str(input("\nIngrese el número de identificación del estudiante: "))
            if numid.strip()=="":
                print("\nEl número de identificación no debe de estar vacío. Intentelo de nuevo.")
            else:
                numid=int(numid)
                if numid in estudiantes:
                    print("\nYa está registrado ese número de identificación. Intentelo de nuevo.")
                else:
                    condicionid=True
        condicionnom=False
        while condicionnom==False:
            nombre=str(input("Ingrese el nombre del estudiante: "))
            if nombre.strip()=="":
                print("\nEl nombre no debe quedar vacío. Intentelo de nuevo.\n")
            else:
                condicionnom=True
        
        
        condicion1=False
        while condicion1==False:
            c=str(input("\nIngrese la primera calificación del alumno: "))
            if c.strip()=="":
                print("La primera calificación no debe de quedar vacía. Intentelo de nuevo.")
            else:
                c=int(c)
                if c>=0 and c<=100:
                    c1=c
                    condicion1=True
                    print("\nCalificación agregada con éxito :)\n")
                else:
                    print("\nCalificación fuera de rango (debe ser de 0 a 100). Intentelo de nuevo.")

        condicion2=False
        while condicion2==False:
            c=str(input("Ingrese la segunda calificación del alumno: "))
            if c.strip()=="":
                print("La segunda calificación no debe de quedar vacía. Intentelo de nuevo.")
            else:
                c=int(c)
                if c>=0 and c<=100:
                    c2=c
                    condicion2=True
                    print("\nCalificación agregada con éxito :)\n")
                else:
                    print("\nCalificación fuera de rango (debe ser de 0 a 100). Intentelo de nuevo.\n")

        condicion3=False
        while condicion3==False:
            c=str(input("Ingrese la tercera calificación del alumno: "))
            if c.strip()=="":
                print("La tercera calificación no debe de quedar vacía. Intentelo de nuevo.")
            else:
                c=int(c)
                if c>=0 and c<=100:
                    c3=c
                    condicion3=True
                    print("\nCalificación agregada con éxito :)")
                else:
                    print("\nCalificación fuera de rango (debe ser de 0 a 100). Intentelo de nuevo.\n")
        calificaciones=(c1,c2,c3)            
        estudiantes[numid]=nombre
        conta,contr,riesgorep,acumprom=registrar(estudiantes,calificaciones,conta,contr,riesgorep,acumprom)
    elif opcion==2:
        mostrar()
    elif opcion==3:
        consultar()
    elif opcion==4:
        estadisticas(estudiantes)
    elif opcion==5:
        print("Saliendo del sistema...")
        break
    else:
        print("Opción no válida. Intentelo de nuevo.")
