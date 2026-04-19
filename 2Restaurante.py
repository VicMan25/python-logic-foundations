#Menus
precio_basico = 50000
precio_premium = 100000
precio_personalizado = 150000
precio_menu_infantil=30000

#Impuesto/Descuento
impuesto = 0.10
descuento = 0.05

#Propina segun tipo de menú
propina_basico = 0.10
propina_premium = 0.15
propina_personalizado = 0.20
ppropina_menu_infantil = 0.10

menu = input("Ingrese el tipo de menú (basico, premium, personalizado, infantil): ").lower()
personas = int(input("Ingrese el número de personas: "))

if menu == "basico":
    precio = precio_basico
    propina = propina_basico
elif menu == "premium":
    precio = precio_premium
    propina = propina_premium
elif menu == "personalizado":
    precio = precio_personalizado
    propina = propina_personalizado
elif menu == "infantil":
    precio = precio_menu_infantil
    propina = precio_menu_infantil
else:
    print("Menú no válido.")
    exit()

subtotal = precio * personas
monto_impuesto = subtotal * impuesto
monto_propina = subtotal * propina
monto_descuento = subtotal * descuento if personas > 5 else 0
total = subtotal + monto_impuesto + monto_propina - monto_descuento

print("\n--- RESUMEN DE LA CUENTA ---")
print(f"Subtotal: ${subtotal:,.2f}")
print(f"Impuesto (10%): ${monto_impuesto:,.2f}")
print(f"Propina ({propina*100}%): ${monto_propina:,.2f}")
print(f"Descuento aplicado (5% si >5 personas): -${monto_descuento:,.2f}")
print(f"TOTAL A PAGAR: ${total:,.2f}")
