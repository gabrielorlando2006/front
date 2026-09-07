def buscar_alumno(nombre_buscar):

    for alumno in alumnos:

        if alumno["nombre"].lower() == nombre_buscar.lower():

            print("Nombre:", alumno["nombre"])
            print("Materia:", alumno["materia"])
            print("Edad:", alumno["edad"])

            return

    print("Alumno no encontrado")


nombre_ingresado = input("Buscar alumno: ")

buscar_alumno(nombre_ingresado)