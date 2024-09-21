# En este ejercicio, tendrán total libertad para elegir la problemática y la mejor solución. 
# Cada grupo podrá decidir su propio enfoque y desarrollar el software según sus criterios.
# El grupo que presente la mejor solución será el único en recibir los 60 puntos asignados a esta pregunta.
alimentos_calorias = {
    "manzana": 40,
    "platano": 51,
    "pollo": 190,
    "arroz": 100,
    "ensalada": 15,
    "pan": 210,
    "huevo": 75
}

def mostrar_menu():
    print("---- Calculadora de Calorías ----")
    print("1. Ingresar alimento")
    print("2. Mostrar total de calorías")
    print("3. Recomendaciones")
    print("4. Salir")

def ingresar_alimento(calorias_totales):
    alimento = input("Ingrese el nombre del alimento: ").lower()
    cantidad = int(input("Ingrese la cantidad (en porciones): "))
    
    if alimento in alimentos_calorias:
        calorias = alimentos_calorias[alimento] * cantidad
        calorias_totales += calorias
        print(f"{alimento.title()} agregado. Calorías: {calorias}")
    else:
        print("Alimento no encontrado. Por favor, intente con otro.")

    return calorias_totales

def mostrar_total(calorias_totales):
    print(f"Total de calorías consumidas: {calorias_totales}")

def recomendaciones(calorias_totales):
    if calorias_totales < 1000:
        print("Recomendación: ¡Aumenta tu ingesta calórica!")
    elif calorias_totales > 1999:
        print("Recomendación: ¡Considera reducir tu ingesta calórica!")
    else:
        print("¡Estás en el rango saludable de calorías!")

def main():
    calorias_totales = 0
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            calorias_totales = ingresar_alimento(calorias_totales)
        elif opcion == "2":
            mostrar_total(calorias_totales)
        elif opcion == "3":
            recomendaciones(calorias_totales)
        elif opcion == "4":
            print("Saliendo de la aplicación. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
