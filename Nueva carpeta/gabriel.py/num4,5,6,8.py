alumnos = [
    {
        "nombre": "Juan",
        "materia": "Programacion",
        "edad": 16
    },
    {
        "nombre": "Maria",
        "materia": "Matematica",
        "edad": 17
    },
    {
        "nombre": "Lucas",
        "materia": "Base de Datos",
        "edad": 15
    },
    {
        "nombre": "Sofia",
        "materia": "Ingles",
        "edad": 18
    },
    {
        "nombre": "Martin",
        "materia": "Redes",
        "edad": 16
    }
]

for alumno in alumnos:
    print(alumno["nombre"], "-", alumno["materia"])
    print("Cantidad total de alumnos:", len(alumnos))

mayores = 0

for alumno in alumnos:
    if alumno["edad"] > 16:
        mayores += 1

print("Cantidad de alumnos mayores de 16:", mayores)