def seleccionar_materia() -> str:
    opcion = 0
    while opcion < 1 or opcion > 6:
        print("""
                    1- Programación I
                    2- Programación II
                    3- Programación III
                    4- Laboratorio de Computación I
                    5- Laboratorio de Computación II
                    6- Laboratorio de Computación III
                    """)
        opcion = int(input("Seleccione una opcion: "))

        if opcion == 1:
            return "Programación I"
        elif opcion == 2:
            return "Programación II"
        elif opcion == 3:
            return "Programación III"
        elif opcion == 4:
            return "Laboratorio de Computación I"
        elif opcion == 5:
            return "Laboratorio de Computación II"
        elif opcion == 6:
            return "Laboratorio de Computación III"
        else:
            print("Opcion incorrecta")