buscar = input("Ingresá el nombre del alumno: ")

encontrado = False

for alumno in alumnos:
    if alumno["nombre"].lower() == buscar.lower():
        print("Nombre:", alumno["nombre"])
        print("Materia:", alumno["materia"])
        print("Edad:", alumno["edad"])
        encontrado = True

if encontrado == False:
    print("Alumno no encontrado")