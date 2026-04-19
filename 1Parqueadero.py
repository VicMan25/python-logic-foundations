def aplicar_descuento(precio):
    if precio >= 100000 and precio <= 200000:
        return precio - (precio * 0.1)
    elif precio > 200000:
        return precio - (precio * 0.5)
    else:
        return precio
    
def calcularPagoPorHora(horas, tarifa):
    return horas * tarifa

def calcularPagoPorDia(dias, tarifa_diaria):
    total = dias * tarifa_diaria
    if dias > 1:
        total += total * 0.25  # Penalidad del 25% si supera 24 horas
    if dias > 2:
        total -= total * 0.15  # Descuento del 15% si supera 48 horas
    return total

print("=====Bienvenido Al Parqueadero VicDav=====\n 1. Automóvil \n 2. Camioneta \n 3. Camión")
vehiculo = int(input("Ingrese la opción que corresponda a su tipo de vehículo: \n"))

tarifas = {
    1: {'tarifa_hora': 5000, 'tarifa_dia': 40000},
    2: {'tarifa_hora': 8000, 'tarifa_dia': 60000},
    3: {'tarifa_hora': 12000, 'tarifa_dia': 80000}
}

if vehiculo in tarifas:
    print("¿Gustas dejar el vehículo horas o días? \n 1. Días \n 2. Horas \n 3. No quiero este servicio, chao")
    opcion = int(input("Ingrese su respuesta: \n"))
    
    if opcion == 1:
        dias = int(input("¿Cuántos días gustas dejar tu vehículo?: \n"))
        total_pago = calcularPagoPorDia(dias, tarifas[vehiculo]['tarifa_dia'])
    elif opcion == 2:
        horas = int(input("¿Cuántas horas gustas dejar tu vehículo?: \n"))
        if horas <= 8:
            total_pago = calcularPagoPorHora(horas, tarifas[vehiculo]['tarifa_hora'])
        else:
            total_pago = tarifas[vehiculo]['tarifa_dia']
    else:
        print("Gracias por usar nuestro servicio")
        exit()
    
    festivo = input("¿Es fin de semana o festivo? (S/N): \n").lower()
    if festivo == 'S':
        total_pago += total_pago * 0.2
    
    frecuente = input("¿Eres cliente frecuente? (S/N): \n").lower()
    if frecuente == 'S':
        total_pago -= total_pago * 0.1
    
    print(f"El total a pagar es: ${total_pago:}")
else:
    print("Opción incorrecta. Intente nuevamente.")
