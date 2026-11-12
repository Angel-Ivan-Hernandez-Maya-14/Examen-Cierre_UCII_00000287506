def menu():
    print("\n=====MENU DE OPCIONES=====")
    print("1. Registrar un estudiante")
    print("2. Mostrar todos los estudiantes registrados")
    print("3. Consultar el promedio de un estudiante")
    print("4. Mostrar estadísticas generales del grupo")
    print("5. Salir del programa")

def registrar(est,califs):
    prom=sum(califs)/3
    if prom>=80 and prom<=100:
        sit="Aprobado"
    elif prom>=70 and prom <=79:
        sit="Riesgo de reprobación. Pero estas aprobado"
    else:
        sit="Reprobado"

    with open("estudiantes.txt","a") as archivo: 
        archivo.write(f"Número de identificación del alumno: {est.keys()}\nNombre del alumno: {est.values()}\nPrimera calificación: {califs[0]}\nSegunda calificación: {califs[1]}\nTercera calificación: {califs[2]}\nPromedio: {prom}\nSituación: {sit}")

print("\n=====SISTEMA DE REGISTRO Y ANÁLISIS DE ESTUDIANTES=====")
print("Sea bienvenido :)")
print("A continuación se mostrará el menú de las opciones que puede hacer en el sistema")
print("En caso de que la opción no sea válida, se volverá a mostrar el menú hasta que la opción sea válida")

while True:
    menu()
    opcion=int(input("¿Qué acción desea realizar? "))
    if opcion==1:
        numid=int(input("Ingrese el número de identificación del estudiante: "))
        nombre=str(input("Ingrese el nombre del estudiante: "))
        estudiantes={numid:nombre}
        condicion1=False
        while condicion1==False:
            c=int(input("Ingrese la primera calificación del alumno: "))
            if c>=0 and c<=100:
                c1=c
                condicion1=True
                print("\nCalificación agregada con éxito :)\n")
            else:
                print("\nCalificación fuera de rango (debe ser de 0 a 100). Intentelo de nuevo.\n")

        condicion2=False
        while condicion2==False:
            c=int(input("Ingrese la segunda calificación del alumno: "))
            if c>=0 and c<=100:
                c2=c
                condicion2=True
                print("\nCalificación agregada con éxito :)\n")
            else:
                print("\nCalificación fuera de rango (debe ser de 0 a 100). Intentelo de nuevo.\n")

        condicion3=False
        while condicion3==False:
            c=int(input("Ingrese la tercera calificación del alumno: "))
            if c>=0 and c<=100:
                c3=c
                condicion3=True
                print("\nCalificación agregada con éxito :)\n")
            else:
                print("\nCalificación fuera de rango (debe ser de 0 a 100). Intentelo de nuevo.\n")

        calificaciones=(c1,c2,c3)
        registrar(estudiantes,calificaciones)
    elif opcion==2:
        print()
    elif opcion==3:
        print()
    elif opcion==4:
        print()
    elif opcion==5:
        print("Saliendo del sistema...")
        break
    else:
        print("Opción no válida. Intentelo de nuevo.")