
# Bucle principal
while True:
    # Mostrar el menú con el formato solicitado
    print("\nCONVERSION DE MONEDA\n")

    print("1. Convertir pesos a dólares")
    print("2. Convertir dólares a pesos")
    print("3. Salir")
    opcion = input("Elige una opcion: ")
    

    if opcion == "1":
        # Opción para convertir de Pesos a Dólares
        pesos = float(input("Introduce la cantidad en pesos: "))
        TC = float(input("Introduce el TC actual: "))
        dll = pesos / TC
        print(f"${pesos:.2f} mx son ${dll:.2f} dólares.")

    elif opcion == "2":
        # Opción para convertir de Dólares a Pesos
        dll = float(input("Introduce la cantidad en dólares: "))
        TC = float(input("Introduce el tTC actual: "))
        pesos = dll * TC
        print(f"${dll:.2f} dólares son a ${pesos:.2f} pesos mx.")

    elif opcion == "3":
        # Opción para salir del programa
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida. Por favor, elige una opción válida.")

