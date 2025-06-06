def mostrar_menu_principal():
    print("MENU PRINCIPAL")
    print("1. Ver información del sistema")
    print("2. Gestión de parcela")
    print("3. Gestión del sensor")
    print("4. Registro de mediciones")
    print("5. Salir")

def gestion_parcela():
    while True:
        print("Usted seleccionó la opción 2: Gestión de parcela")
        print("1) Registrar parcela")
        print("2) Listar parcelas")
        print("3) Volver al MENU PRINCIPAL")
        sub_opcion = input("Seleccione una opción: ")

        if sub_opcion == "1":
            nombre = input("Ingrese el nombre de la parcela: ")
            ubicacion = input("Ingrese la ubicación de la parcela: ")
            parcela = {"nombre": nombre, "ubicacion": ubicacion}
            parcelas.append(parcela)
            print("Parcela registrada con éxito.")

        elif sub_opcion == "2":
            if not parcelas:
                print("No hay parcelas registradas.")
            else:
                print("Parcelas registradas:")
                for i, p in enumerate(parcelas, 1):
                    print(f"{i}. Nombre: {p['nombre']}, Ubicación: {p['ubicacion']}")

        elif sub_opcion == "3":
            break
        else:
            print("Opción inválida. Intente nuevamente.")

def gestion_sensor():
    while True:
        print("Usted seleccionó la opción 3: Gestión del sensor")
        print("1) Registrar tipos de sensores")
        print("2) Sensores instalados")
        print("3) Volver al MENU PRINCIPAL")
        sub_opcion = input("Seleccione una opción: ")

        if sub_opcion == "1":
            tipo = input("Ingrese el tipo de sensor (ej. Humedad, Temperatura): ")
            descripcion = input("Ingrese una breve descripción: ")
            sensor = {"tipo": tipo, "descripcion": descripcion}
            sensores.append(sensor)
            print("Tipo de sensor registrado.")

        elif sub_opcion == "2":
            if not sensores:
                print("No hay sensores registrados.")
            else:
                print("Sensores instalados:")
                for i, s in enumerate(sensores, 1):
                    print(f"{i}. Tipo: {s['tipo']}, Descripción: {s['descripcion']}")

        elif sub_opcion == "3":
            break
        else:
            print("Opción inválida. Intente nuevamente.")

def registro_mediciones():
    while True:
        print("Usted seleccionó la opción 4: Registro de mediciones")
        print("1) Ver mediciones registradas")
        print("2) Agregar nueva medición")
        print("3) Volver al MENU PRINCIPAL")
        sub_opcion = input("Seleccione una opción: ")

        if sub_opcion == "1":
            if not mediciones:
                print("No hay mediciones registradas.")
            else:
                print("Mediciones registradas:")
                for i, m in enumerate(mediciones, 1):
                    print(f"{i}. Sensor: {m['sensor']}, Valor: {m['valor']}, Unidad: {m['unidad']}")

        elif sub_opcion == "2":
            sensor = input("Ingrese el tipo de sensor utilizado: ")
            valor = input("Ingrese el valor medido: ")
            unidad = input("Ingrese la unidad de medida (ej. °C, %, etc.): ")
            medicion = {"sensor": sensor, "valor": valor, "unidad": unidad}
            mediciones.append(medicion)
            print("Medición registrada.")

        elif sub_opcion == "3":
            break
        else:
            print("Opción inválida. Intente nuevamente.")

# ------------------------------
# Programa principal (main loop)
# ------------------------------

print("Bienvenidos al Sistema de Monitoreo - AgroTech")
print("Cooperativa Agrícola Local")

parcelas = []
sensores = []
mediciones = []

while True:
    mostrar_menu_principal()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        print("Este sistema permite monitorear parcelas agrícolas.")
        print("Puede simular registros y consultas simples.")

    elif opcion == "2":
        gestion_parcela()

    elif opcion == "3":
        gestion_sensor()

    elif opcion == "4":
        registro_mediciones()

    elif opcion == "5":
        print("Saliendo del sistema... Gracias por usar AgroTech.")
        break

    else:
        print("Opción inválida. Intente nuevamente.")

        
