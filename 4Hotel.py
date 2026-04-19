#Precios por temporada y tipo de habitación
costo_estandar = 200000
costo_suite = 350000
costo_presidencial = 600000
costo_cuotas = 0.5

#Costos adicionales
costo_desayuno = 20000
costo_spa = 50000

#Descuento
descuento_7_noches = 0.15

temporada = input("Ingrese la temporada (alta, media, baja): ").lower()
habitacion = input("Ingrese el tipo de habitación (estandar, suite, presidencial): ").lower()
noches = int(input("Ingrese el número de noches: "))
incluye_desayuno = input("¿Desea incluir desayuno? (si/no): ").lower() == "si"
incluye_spa = input("¿Desea incluir spa? (si/no): ").lower() == "si"
pago_a_cuotas = input("¿Desea pagar a cuotas(si/no): ").lower() == "si"

if habitacion == "estandar":
    precio_noche = costo_estandar
    costo_spa = 50000
    costo_desayuno = 20000
elif habitacion == "suite":
    precio_noche = costo_suite
    costo_spa = 80000
    costo_desayuno = 30000
elif habitacion == "presidencial":
    precio_noche = costo_presidencial
    costo_spa = 120000
    costo_desayuno = 50000
else:
    print("Tipo de habitación no válido.")
    exit()

subtotal = precio_noche * noches

#Servicios Adicionales
costo_adicional = 0
if incluye_desayuno:
    costo_adicional += costo_desayuno * noches
if incluye_spa:
    costo_adicional += costo_spa * noches

#Descuento + de 7 noches
monto_descuento = (subtotal + costo_adicional) * descuento_7_noches + costo_cuotas if noches > 7 else 0 if pago_a_cuotas == "si" else 0

#Total
total = subtotal + costo_adicional - monto_descuento

print("\n--- RESUMEN DE LA RESERVA ---")
print(f"Subtotal por noches: ${subtotal:,.2f}")
print(f"Servicios adicionales: ${costo_adicional:,.2f}")
print(f"Descuento aplicado (15% si >7 noches): -${monto_descuento:,.2f}")
print(f"TOTAL A PAGAR: ${total:,.2f}")
