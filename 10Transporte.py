#KM/s según el tipo de vehículo
costo_sedan = 2000
costo_suv = 3500
costo_minivan = 5000

#Recargo nocturno/descuento grupal
recargo_nocturno = 0.20
descuento_grupal = 0.10

tipo_vehiculo = input("Ingrese el tipo de vehículo (sedan, suv, minivan): ").lower()
distancia = float(input("Ingrese la distancia en km: "))
horario_nocturno = input("¿El viaje es nocturno? (si/no): ").lower() == "si"
num_personas = int(input("Ingrese el número de personas en el viaje: "))

#Costo segun vehiculo
if tipo_vehiculo == "sedan":
    costo_por_km = costo_sedan
elif tipo_vehiculo == "suv":
    costo_por_km = costo_suv
elif tipo_vehiculo == "minivan":
    costo_por_km = costo_minivan
else:
    print("Tipo de vehículo no válido.")
    exit()

#Calcular costo base del viaje
costo_base = distancia * costo_por_km

#Recargo nocturno
costo_recargo = 0
if horario_nocturno:
    costo_recargo = costo_base * recargo_nocturno

#Descuento si hay mas de 5 personas
descuento = 0
if num_personas > 5:
    descuento = costo_base * descuento_grupal

#Costo final
costo_total = costo_base + costo_recargo - descuento

print("\n--- RESUMEN DEL VIAJE ---")
print(f"Costo base del viaje: ${costo_base:,.2f}")
print(f"Recargo nocturno: ${costo_recargo:,.2f}")
print(f"Descuento por grupo: -${descuento:,.2f}")
print(f"TOTAL A PAGAR: ${costo_total:,.2f}")
