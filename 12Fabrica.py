#Costos por unidad según el turno y el tipo de material
costo_diurno_estandar = 50
costo_diurno_premium = 80
costo_nocturno_estandar = 60
costo_nocturno_premium = 90

#Descuento
descuento_produccion = 0.05

turno = input("Ingrese el turno (diurno/nocturno): ").lower()
tipo_material = input("Ingrese el tipo de material (estandar/premium): ").lower()
cantidad = int(input("Ingrese la cantidad a producir: "))

#Costo por unidad segun el turno y material
if turno == "diurno":
    if tipo_material == "estandar":
        costo_por_unidad = costo_diurno_estandar
    elif tipo_material == "premium":
        costo_por_unidad = costo_diurno_premium
    else:
        print("Tipo de material no válido.")
        exit()
elif turno == "nocturno":
    if tipo_material == "estandar":
        costo_por_unidad = costo_nocturno_estandar
    elif tipo_material == "premium":
        costo_por_unidad = costo_nocturno_premium
    else:
        print("Tipo de material no válido.")
        exit()
else:
    print("Turno no válido.")
    exit()

#Costo total de produccion
costo_total = cantidad * costo_por_unidad

#Descuento si > 1000 unidades
descuento = 0
if cantidad > 1000:
    descuento = costo_total * descuento_produccion

#Costo final con descuento aplicado
costo_final = costo_total - descuento

print("\n--- RESUMEN DE COSTOS ---")
print(f"Costo base de producción: ${costo_total:,.2f}")
print(f"Descuento aplicado: -${descuento:,.2f}")
print(f"TOTAL A PAGAR: ${costo_final:,.2f}")
