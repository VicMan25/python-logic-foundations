consumo_ligero = 0.1
consumo_potencia = 0.2

costo_litro_estandar = 5000
costo_litro_alto_rendimiento = 8000

penalidad_por_exceso = 0.10
bonificacion_vuelta_rapida_ligero = 20000
bonificacion_vuelta_rapida_potencia = 50000

tipo_auto = input("Ingrese el tipo de auto (ligero o potencia): ").lower()
tipo_combustible = input("Ingrese el tipo de combustible (estandar o alto rendimiento): ").lower()
distancia = float(input("Ingrese la distancia de la carrera en km: "))
vueltas_rapidas = int(input("Ingrese el número de vueltas rápidas realizadas: "))
desgaste_neumaticos = float(input("Ingrese el porcentaje de desgaste de neumáticos (0 a 100): "))
exceso_pits = input("¿Hubo exceso de tiempo en pits? (si/no): ").lower() == "si"

if tipo_auto == "ligero":
    consumo = consumo_ligero
    bonificacion = bonificacion_vuelta_rapida_ligero
elif tipo_auto == "potencia":
    consumo = consumo_potencia
    bonificacion = bonificacion_vuelta_rapida_potencia
else:
    print("Tipo de auto no válido.")
    exit()

#Costo del combustible
if tipo_combustible == "estandar":
    costo_combustible = costo_litro_estandar
elif tipo_combustible == "alto rendimiento":
    costo_combustible = costo_litro_alto_rendimiento
else:
    print("Tipo de combustible no válido.")
    exit()

#Consumo de combustible y costo
total_combustible = consumo * distancia
costo_total_combustible = total_combustible * costo_combustible

#Penalidad por desgaste de 50%
penalidad_neumaticos = 0
if desgaste_neumaticos > 50:
    penalidad_neumaticos = costo_total_combustible * penalidad_por_exceso

#Exceso de tiempo en pits
penalidad_pits = 0
if exceso_pits:
    penalidad_pits = costo_total_combustible * penalidad_por_exceso

#Bonificación por vuelta rápida
bonificacion_total = vueltas_rapidas * bonificacion

subtotal = costo_total_combustible + penalidad_neumaticos + penalidad_pits
total = subtotal - bonificacion_total

print("\n--- RESUMEN DE LA CARRERA ---")
print(f"Consumo total de combustible: {total_combustible:.2f} L")
print(f"Costo total de combustible: ${costo_total_combustible:,.2f}")
print(f"Penalidad por neumáticos: ${penalidad_neumaticos:,.2f}")
print(f"Penalidad por pits: ${penalidad_pits:,.2f}")
print(f"Bonificación por vueltas rápidas: -${bonificacion_total:,.2f}")
print(f"TOTAL A PAGAR: ${total:,.2f}")
