import materias as m
alumnos_regulares = []

def registrar_alumno():
    nombre = input("Ingresar el nombre del alumno: ")
    legajo = int(input("Ingresar el legajo del alumno: "))

    antiguedad_en_meses = 0
    while antiguedad_en_meses <= 12:
        antiguedad_en_meses = int(input("Ingresar la antiguedad del alumno en meses (debe ser mayor a 12): "))
    
    nuevo_alumno = {
        'nombre': nombre,
        'legajo': legajo,
        'materias_aprobadas': [],
        'antiguedad': antiguedad_en_meses
    }

    alumnos_regulares.append(nuevo_alumno)


def agregar_materia_aprobada():
    legajo = int(input("Ingresar el legajo del alumno a buscar: "))
    encontrado = False

    for alumno in alumnos_regulares:
        if alumno['legajo'] == legajo:
            encontrado = True
            opcion = 0

            while opcion != 2:
                print("""
                      1-Agregar materia.
                      2-Salir
                      """)
                opcion = int(input("Ingresar una opcion: "))
                if opcion == 1:
                    materia = m.seleccionar_materia()
                    alumno['materias_aprobadas'].append(materia)
                elif opcion == 2:
                    print("Saliendo al menu...")
                else:
                    print ("Opcion incorrecta.")

    if encontrado == False:
        print("Alumno no encontrado.")


def resumen():
    print(f"Cantidad de alumnos evaluados: {len(alumnos_regulares)}")
    for alumno in alumnos_regulares:
        print(f"Alumno: {alumno['nombre']} - Legajo: {alumno['legajo']} - Antiguedad: {alumno['antiguedad']} meses")
        print(f"Cursos: {alumno['materias_aprobadas']}")
        print(f"Cantidad materias aprobadas: {len(alumno['materias_aprobadas'])}")

opcion = 0
while opcion !=4:
    print("""
      1-Registrar alumno.
      2-Agregar materia aprobada.
      3-Mostrar resumen.
      4-Salir.
      """)
    
    opcion = int(input("Ingresar una opcion: "))
    if opcion == 1:
        registrar_alumno()
    elif opcion == 2:
        agregar_materia_aprobada()
    elif opcion == 3:
        resumen()
    elif opcion == 4:
        print("Saliendo...")
    else:
        print("La opcion es incorrecta.")


                    




