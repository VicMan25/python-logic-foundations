from datetime import date
import os

class Cliente:
    contador_id = 1
    
    def __init__(self, nombre, telefono, correo, membresia, dias_membresia, atrasado=False):
        self.id_cliente = Cliente.contador_id
        Cliente.contador_id += 1
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo
        self.membresia = membresia
        self.estado_pago = "Al día" if not atrasado else "Atrasado"
        self.dias_membresia = dias_membresia
        self.historial_asistencia = []
        self.cancelaciones = [] 
    
    def actualizar_datos(self, nombre=None, telefono=None, correo=None, membresia=None):
        if nombre:
            self.nombre = nombre
        if telefono:
            self.telefono = telefono
        if correo:
            self.correo = correo
        if membresia:
            self.membresia = membresia
    
    def registrar_asistencia(self):
        self.historial_asistencia.append(date.today())
    
    def obtener_asistencias_mensuales(self):
        inicio_mes = date.today().replace(day=1)
        return sum(1 for d in self.historial_asistencia if d >= inicio_mes)
    
    def actualizar_estado_pago(self):
        self.estado_pago = "Al día" if self.estado_pago == "Atrasado" else "Atrasado"
    
    def registrar_cancelacion(self, motivo):
        self.cancelaciones.append((date.today(), motivo))
        print(f"Cancelación registrada para {self.nombre}. Motivo: {motivo}")
    
    def __str__(self):
        return f"ID: {self.id_cliente} | Nombre: {self.nombre} | Teléfono: {self.telefono} | Membresía: {self.membresia} | Pago: {self.estado_pago}"

class SistemaGym:
    def __init__(self):
        self.clientes = []
    
    def registrar_cliente(self, nombre, telefono, correo, membresia, dias_membresia, atrasado):
        cliente = Cliente(nombre, telefono, correo, membresia, dias_membresia, atrasado)
        self.clientes.append(cliente)
        print("Cliente registrado exitosamente.")
    
    def buscar_cliente(self, id_cliente):
        for cliente in self.clientes:
            if cliente.id_cliente == id_cliente:
                return cliente
        return None
    
    def actualizar_cliente(self, id_cliente, nombre=None, telefono=None, correo=None, membresia=None):
        cliente = self.buscar_cliente(id_cliente)
        if cliente:
            cliente.actualizar_datos(nombre, telefono, correo, membresia)
            print("Cliente actualizado correctamente.")
        else:
            print("Cliente no encontrado.")
    
    def eliminar_cliente(self, id_cliente):
        cliente = self.buscar_cliente(id_cliente)
        if cliente:
            self.clientes.remove(cliente)
            print("Cliente eliminado correctamente.")
        else:
            print("Cliente no encontrado.")
    
    def registrar_asistencia(self, id_cliente):
        cliente = self.buscar_cliente(id_cliente)
        if cliente:
            if cliente.estado_pago == "Al día":
                cliente.registrar_asistencia()
                print("Asistencia registrada correctamente.")
            else:
                print("No se puede registrar asistencia. El cliente tiene pagos atrasados.")
    
    def obtener_asistencias_mensuales(self, id_cliente):
        cliente = self.buscar_cliente(id_cliente)
        if cliente:
            print(f"Asistencias este mes para {cliente.nombre}: {cliente.obtener_asistencias_mensuales()}")
        else:
            print("Cliente no encontrado.")
    
    def registrar_pago(self, id_cliente):
        cliente = self.buscar_cliente(id_cliente)
        if cliente:
            cliente.actualizar_estado_pago() 
            print(f"Estado de pago de {cliente.nombre} cambiado a: {cliente.estado_pago}")
        else:
            print("Cliente no encontrado.")
    
    def aplicar_descuento(self, id_cliente):
        cliente = self.buscar_cliente(id_cliente)
        if cliente:
            if cliente.estado_pago == "Atrasado":
                print(f"{cliente.nombre} tiene pagos pendientes. No se puede aplicar descuento.")
                return
            descuento = 0
            if cliente.obtener_asistencias_mensuales() >= 3:
                descuento += 0.5  
            if cliente.dias_membresia >= 180:
                descuento += 0.05 
            print(f"Descuento aplicado a {cliente.nombre}: {descuento * 100}%")
        else:
            print("Cliente no encontrado.")
    
    def cancelar_membresia(self, id_cliente, motivo):
        cliente = self.buscar_cliente(id_cliente)
        if cliente:
            cliente.registrar_cancelacion(motivo)
            self.eliminar_cliente(id_cliente)
        else:
            print("Cliente no encontrado.")
    
    def listar_clientes(self):
        if not self.clientes:
            print("No hay clientes registrados.")
            return
        for cliente in self.clientes:
            print(cliente)
            
    def mostrar_motivos_cancelacion(self):
        print("\n=== Motivos de Cancelación Registrados ===")
        motivos_registrados = False
        for cliente in self.clientes:
            if cliente.cancelaciones:
                print(f"\nCliente: {cliente.nombre} (ID: {cliente.id_cliente})")
                for fecha, motivo in cliente.cancelaciones:
                    print(f"- [{fecha}]: {motivo}")
        
        if not any(cliente.cancelaciones for cliente in self.clientes):
            print("No hay motivos de cancelación registrados.")

    

def mostrar_menu():
    sistema = SistemaGym()
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n=== GYM POWER FIT ===")
        print("1. Registrar cliente")
        print("2. Actualizar cliente")
        print("3. Eliminar cliente")
        print("4. Registrar asistencia")
        print("5. Ver asistencias del mes")
        print("6. Cambiar estado de pago")
        print("7. Aplicar descuento")
        print("8. Cancelar membresía")
        print("9. Listar clientes")
        print("10. Motivos de Cancelación")
        print("11. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            nombre = input("Nombre: ")
            telefono = input("Teléfono: ")
            correo = input("Correo: ")
            membresia = input("Tipo de membresía: ")
            dias_membresia = int(input("Días de membresía: "))
            atrasado = input("¿Tiene pagos atrasados? (s/n): ").lower() == 's'
            sistema.registrar_cliente(nombre, telefono, correo, membresia, dias_membresia, atrasado)
        
        elif opcion == "2":
            id_cliente = int(input("ID del cliente a actualizar: "))
            nombre = input("Nuevo nombre: ")
            telefono = input("Nuevo teléfono: ")
            correo = input("Nuevo correo: ")
            membresia = input("Nuevo tipo de membresía: ")
            sistema.actualizar_cliente(id_cliente, nombre or None, telefono or None, correo or None, membresia or None)
        
        elif opcion == "3":
            id_cliente = int(input("Ingrese el ID del cliente a eliminar: "))
            sistema.eliminar_cliente(id_cliente)
        
        elif opcion == "4":
            id_cliente = int(input("Ingrese el ID del cliente: "))
            sistema.registrar_asistencia(id_cliente)
        
        elif opcion == "5":
            id_cliente = int(input("Ingrese el ID del cliente: "))
            sistema.obtener_asistencias_mensuales(id_cliente)
        
        elif opcion == "6":
            id_cliente = int(input("Ingrese el ID del cliente para cambiar el estado de pago: "))
            sistema.registrar_pago(id_cliente)
        
        elif opcion == "7":
            id_cliente = int(input("Ingrese el ID del cliente: "))
            sistema.aplicar_descuento(id_cliente)
        
        elif opcion == "8":
            id_cliente = int(input("Ingrese el ID del cliente a cancelar: "))
            motivo = input("Ingrese el motivo de la cancelación: ")
            sistema.cancelar_membresia(id_cliente, motivo)
        
        elif opcion == "9":
            sistema.listar_clientes()
            
        elif opcion == "10": 
            sistema.mostrar_motivos_cancelacion()    
        
        elif opcion == "11":
            break
        
        else:
            print("Opción no válida. Intente de nuevo.")
        
        input("Presione Enter para continuar...")

if __name__ == "__main__":
    mostrar_menu()