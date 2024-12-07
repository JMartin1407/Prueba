# Importar la clase Tinaco
from Tinaco import Tinaco

# Lista para almacenar los tinacos
tinacos = []

# Función para agregar un nuevo tinaco
def agregarTinacos():
    try:
        capLts = int(input("Ingresa la capacidad del tinaco en litros: "))
        contLts = int(input("Ingrese el contenido inicial que tendrá el tinaco en litros: "))
        nuevo_tinaco = Tinaco(capLts, contLts)
        tinacos.append(nuevo_tinaco)
        print("El tinaco se agregó de manera correcta.")
    except ValueError:
        print("Ingresar únicamente valores enteros.")

# Función para mostrar la lista de tinacos
def mostrarTinacos():
    if not tinacos:
        print("Actualmente no hay tinacos registrados.")
    else:
        for i, tinaco in enumerate(tinacos, start=1):
            print(f"{i}. Capacidad: {tinaco.capLts} litros, Contenido: {tinaco.contLts} litros")
        print(f"\nTotal de tinacos: {len(tinacos)}")

# Función principal de menú de opciones
def menuTinacos():
    while True:
        print("\n--- Menú de Tinacos ---")
        print("1.- Agregar Tinaco")
        print("2.- Mostrar Tinacos")
        print("3.- Seleccionar Tinaco para gestionar")
        print("4.- Salir")

        opc = input("Selecciona una opción: ")

        if opc == "1":
            agregarTinacos()
        elif opc == "2":
            mostrarTinacos()
        elif opc == "3":
            seleccionar_tinaco()
        elif opc == "4":
            print("Fin del programa.")
            break
        else:
            print("Opción no válida, intente de nuevo.")

# Función para seleccionar un tinaco específico
def seleccionar_tinaco():
    if not tinacos:
        print("No existen tinacos en la lista.")
        return

    mostrarTinacos()
    try:
        seleccion = int(input("Seleccione el número de un tinaco para gestionar: ")) - 1
        if 0 <= seleccion < len(tinacos):
            gestionarTinacos(seleccion)
        else:
            print("Selección no válida.")
    except ValueError:
        print("Por favor, ingrese un número válido.")

# Función de gestión del tinaco seleccionado
def gestionarTinacos(indice):
    tinaco_seleccionado = tinacos[indice]
    
    while True:
        print("\n--- Gestión del Tinaco ---")
        print("1.- Llenar")
        print("2.- Vaciar")
        print("3.- Eliminar")
        print("4.- Regresar al menú principal")

        opc = input("Selecciona una opción: ")

        if opc == "1":
            llenar_tinaco(tinaco_seleccionado)
        elif opc == "2":
            vaciar_tinaco(tinaco_seleccionado)
        elif opc == "3":
            confirmar_eliminar_tinaco(indice)
            break
        elif opc == "4":
            break
        else:
            print("Opción no válida, intente de nuevo.")

# Función para llenar el tinaco
def llenar_tinaco(tinaco):
    try:
        litros = int(input("Ingrese la cantidad de litros para llenar: "))
        
        # Verificar si los litros exceden la capacidad del tinaco
        if tinaco.contLts + litros > tinaco.capLts:
            sobrante = (tinaco.contLts + litros) - tinaco.capLts
            print(f"El tinaco se ha llenado por completo. No se puede agregar {sobrante} litros adicionales.")
            tinaco.contLts = tinaco.capLts  # El tinaco se llena completamente
        else:
            nuevo_contenido = tinaco.llenar(litros)
            print(f"Contenido actual del tinaco: {nuevo_contenido} litros")
    except ValueError:
        print("Ingrese un valor entero para los litros.")

# Función para vaciar el tinaco
def vaciar_tinaco(tinaco):
    try:
        litros = int(input("Ingrese la cantidad de litros para vaciar: "))
        nuevo_contenido = tinaco.vaciar(litros)
        print(f"Contenido actual del tinaco: {nuevo_contenido} litros")
    except ValueError:
        print("Ingrese un valor entero para los litros.")

# Función para confirmar la eliminación de un tinaco
def confirmar_eliminar_tinaco(indice):
    confirmacion = input("¿Está seguro de que desea eliminar este tinaco? (s/n): ").lower()
    if confirmacion == 's':
        tinacos.pop(indice)
        print("Tinaco eliminado.")
    else:
        print("No se eliminó el tinaco.")

# Ejecutar el menú principal
menuTinacos()
