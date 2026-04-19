import os
os.system("cls")

def compraEnDolares(valor):
    precioEnDolar = 0
    precioEnDolar = valor/4018
    
    print(f'El precio en dolar del producto es: {precioEnDolar} USD')
    
def sumarNumero(A,B):
    suma = A+B
    print(suma)

while True:
    
    opcion = input(
        "Selecciona una opción:\n"
        "1. Realizar compra\n"
        "2. Cambiar moneda\n"
        "3. Salir\n\n"
        "Ingresa tu elección: "
    )

    if opcion == "1":
        valor = float(input("\nIngresa el monto de la compra: "))
        
        if valor <= 50:
            print(f"\nTotal a pagar: ${valor} (Sin descuento)")
        elif valor <= 100:
            total = valor * 0.9
            print(f"\nDescuento: 10% - Total a pagar: ${total:.2f}")
        elif valor <= 200:
            total = valor * 0.8
            print(f"\nDescuento: 20% - Total a pagar: ${total:.2f}")
        else:
            total = valor * 0.7
            print(f"\nDescuento: 30% - Total a pagar: ${total:.2f}")
            
        input("\nPresiona Enter para continuar...")
        
    elif opcion == "2":
        print("Cambio de moneda, COP -> USD")
        valorAConvertir = float(input("\nDigita el valor a convertir:"))
        
        compraEnDolares(valorAConvertir)    
        
    elif opcion == "3":
        print("\nSaliendo del sistema...")
        break
    
        
    else:
        print("\n⚠ Opción inválida. Intenta nuevamente.")
        input("Presiona Enter para continuar...")