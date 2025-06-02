print("Bienvenidos al Sistema de Monitoreo - AgroTech")
print("Cooperativa Agrícola Local")

while True:
    print("MENU PRINCIPAL")
    print("1. Ver información del sistema")
    print("2. Gestión de parcela")
    print("3. Gestión del sensor")
    print("4. Registro de mediciones")
    print("5. Salir") 
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        print("Este sistema permite monitorear parcelas agrícolas.")
        print("Puede simular registros y consultas simples.")
    
    elif opcion == "2":
        while True:
            print("Usted seleccionó la opción 2: Gestión de parcela")
            print("1) Registrar parcela")
            print("2) Listar parcelas")
            print("3) Volver al MENU PRINCIPAL")
            sub_opcion = input("Seleccione una opción: ")
            
            if sub_opcion == "1":
                print("Función para registrar parcela (a implementar)")
            elif sub_opcion == "2":
                print("Función para listar parcelas (a implementar)")
            elif sub_opcion == "3":
                break
            else:
                print("Opción inválida. Intente nuevamente.")

    elif opcion == "3":
        while True:
            print("Usted seleccionó la opción 3: Gestión del sensor")
            print("1) Registrar tipos de sensores")
            print("2) Sensores instalados")
            print("3) Volver al MENU PRINCIPAL")
            sub_opcion = input("Seleccione una opción: ")

            if sub_opcion == "1":
                print("Función para registrar tipos de sensores (a implementar)")
            elif sub_opcion == "2":
                print("Función para mostrar sensores instalados (a implementar)")
            elif sub_opcion == "3":
                break
            else:
                print("Opción inválida. Intente nuevamente.")

    elif opcion == "4":
        while True:
            print("Usted seleccionó la opción 4: Registro de mediciones")
            print("1) Ver mediciones registradas")
            print("2) Agregar nueva medición")
            print("3) Volver al MENU PRINCIPAL")
            sub_opcion = input("Seleccione una opción: ")

            if sub_opcion == "1":
                print("Función para ver mediciones registradas (a implementar)")
            elif sub_opcion == "2":
                print("Función para agregar nueva medición (a implementar)")
            elif sub_opcion == "3":
                break
            else:
                print("Opción inválida. Intente nuevamente.")

    elif opcion == "5":
        print("Saliendo del sistema... ¡Gracias por usar AgroTech!")
        break

    else:
        print("Opción inválida. Intente nuevamente.")
