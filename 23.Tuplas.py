# Lista global para guardar los estudiantes
estudiantes = []
id = 0  # contador global

def agregarEstudiante():
    global id
    id += 1  # incrementar el id

    nombre = input("Digita el nombre del estudiante: ")
    numeros = int(input("Digita un número celular: "))
    nIdentificacion = int(input("Digita el número de identificación: "))
    email = input("Digita el correo del estudiante: ")

    # Pedir notas
    notas = []
    cantidadNotas = int(input("¿Cuántas notas deseas ingresar para este estudiante? "))
    for i in range(cantidadNotas):
        nota = float(input(f"Digita la nota {i+1}: "))
        notas.append(nota)

    # Guardamos los datos en una lista (incluyendo notas)
    estudiante = [id, nombre, numeros, nIdentificacion, email, notas]
    estudiantes.append(estudiante)

    # Crear la tupla con algunos datos
    tupla = (id, nombre, nIdentificacion)

    print(f"\nLos datos de la tupla son: {tupla}")
    print(f"Los datos completos del estudiante son: {estudiante}\n")


# Menú para repetir
op = int(input("Digita 1 para agregar un estudiante, 0 para salir: "))
while op == 1:
    agregarEstudiante()
    op = int(input("Digita 1 para agregar otro estudiante, 0 para salir: "))

print("\nLista final de estudiantes registrados:")
for est in estudiantes:
    print(est)
