class Pasajero:
    def __init__(self, nombre, edad, destino):
        self.nombre = nombre
        self.edad = edad
        self.destino = destino

    def actualizar_destino(self, nuevo_destino):
        self.destino = nuevo_destino

    def mostrar_info(self):
        print(">> Datos del pasajero")
        print(f"Nombre  : {self.nombre}")
        print(f"Edad    : {self.edad} años")
        print(f"Destino : {self.destino}")
        print("-" * 40)


class SistemaReservas:
    def __init__(self):
        self.reservas_dict = {}
        self.destinos_permitidos = ("New York", "París", "Tokio", "Londres", "Sídney")

    def nueva_reserva(self, nombre, edad, destino):
        try:
            if not nombre or nombre.isspace():
                raise ValueError("El nombre no puede estar vacío o solo con espacios.")

            if nombre in self.reservas_dict:
                raise ValueError("Ya existe una reserva para este pasajero.")

            if not (0 < edad <= 120):
                raise ValueError("Edad inválida. Debe estar entre 1 y 120 años.")

            if destino not in self.destinos_permitidos:
                raise ValueError("Destino no válido. Opciones: " + ", ".join(self.destinos_permitidos))

            self.reservas_dict[nombre] = Pasajero(nombre, edad, destino)
            print(f"[✔] Reserva registrada para: {nombre}")

        except ValueError as error:
            print(f"[Error] {error}")

    def eliminar_reserva(self, nombre_pasajero):
        try:
            if nombre_pasajero not in self.reservas_dict:
                raise ValueError("No existe una reserva con ese nombre.")

            del self.reservas_dict[nombre_pasajero]
            print(f"[✔] Reserva de {nombre_pasajero} eliminada.")

        except ValueError as error:
            print(f"[Error] {error}")

    def mostrar_reservas(self):
        if not self.reservas_dict:
            print("⚠ No hay reservas cargadas en el sistema.")
            return

        print("\n>>> LISTADO ACTUAL DE RESERVAS <<<")
        for pasajero in self.reservas_dict.values():
            pasajero.mostrar_info()

    def destinos_mas_frecuentes(self, cantidad_minima):
        if not self.reservas_dict:
            print("⚠ No hay datos disponibles para análisis.")
            return

        contador = {}
        for reserva in self.reservas_dict.values():
            contador[reserva.destino] = contador.get(reserva.destino, 0) + 1

        print("\n>>> DESTINOS POPULARES <<<")
        populares = False
        for destino, cantidad in contador.items():
            if cantidad >= cantidad_minima:
                print(f"{destino}: {cantidad} reservas")
                populares = True

        if not populares:
            print(f"No hay destinos con al menos {cantidad_minima} reservas.")


def mostrar_menu():
    print("\n=== MENU PRINCIPAL - RESERVAS AÉREAS ===")
    print("1) Crear nueva reserva")
    print("2) Eliminar una reserva")
    print("3) Ver todas las reservas")
    print("4) Consultar destinos populares")
    print("5) Salir del sistema")


def iniciar_aplicacion():
    gestor = SistemaReservas()

    while True:
        mostrar_menu()

        try:
            seleccion = int(input("Seleccione una opción [1-5]: "))

            if seleccion == 1:
                nombre = input("Nombre del pasajero: ").strip()
                edad = int(input("Edad: "))
                destino = input("Destino deseado: ").strip()
                gestor.nueva_reserva(nombre, edad, destino)

            elif seleccion == 2:
                nombre_borrar = input("Nombre de la reserva a cancelar: ").strip()
                gestor.eliminar_reserva(nombre_borrar)

            elif seleccion == 3:
                gestor.mostrar_reservas()

            elif seleccion == 4:
                try:
                    umbral = int(input("Cantidad mínima de reservas para ser popular: "))
                    gestor.destinos_mas_frecuentes(umbral)
                except ValueError:
                    print("Debe ingresar un número válido para el umbral.")

            elif seleccion == 5:
                print("🔚 Cerrando el sistema. ¡Hasta luego!")
                break

            else:
                print("⚠ Opción inválida. Elija entre 1 y 5.")

        except ValueError:
            print("⚠ Entrada no válida. Use solo números enteros.")


if __name__ == "__main__":
    iniciar_aplicacion()
