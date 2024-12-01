from salacine import SalaCine

def menu():
    cine = SalaCine()

    while True:
        print("\nSistema de Reservas para Cine")
        print("1. Agregar asiento")
        print("2. Reservar asiento")
        print("3. Cancelar reserva")
        print("4. Mostrar asientos")
        print("5. Buscar asiento")
        print("6. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            try:
                numero = int(input("Introduce el número del asiento: "))
                fila = input("Introduce la fila del asiento (A, B, C, etc.): ")
                cine.agregar_asiento(numero, fila)
            except ValueError:
                print("Por favor, ingresa un número válido para el asiento.")

        elif opcion == "2":
            try:
                numero = int(input("Introduce el número del asiento: "))
                fila = input("Introduce la fila del asiento: ")
                edad = int(input("Introduce la edad del espectador: "))
                dia = input("Introduce el día de la semana (ej. lunes, miércoles): ")
                cine.reservar_asiento(numero, fila, edad, dia)
            except ValueError:
                print("Por favor, ingresa una edad válida.")

        elif opcion == "3":
            try:
                numero = int(input("Introduce el número del asiento a cancelar: "))
                fila = input("Introduce la fila del asiento: ")
                cine.cancelar_reserva(numero, fila)
            except ValueError:
                print("Por favor, ingresa un número válido para el asiento.")

        elif opcion == "4":
            cine.mostrar_asientos()

        elif opcion == "5":
            try:
                numero = int(input("Introduce el número del asiento: "))
                fila = input("Introduce la fila del asiento: ")
                asiento = cine.buscar_asiento(numero, fila)
                if asiento:
                    print(asiento.mostrar_asiento())
                else:
                    print("Asiento no encontrado.")
            except ValueError:
                print("Por favor, ingresa un número válido para el asiento.")

        elif opcion == "6":
            print("Gracias por usar el sistema de reservas.")
            break

        else:
            print("Opción no válida. Intenta nuevamente.")

if __name__ == "__main__":
    menu()