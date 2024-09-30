import temperatura
import masa
import tiempo

def menu():
    print("Selecciona una categoría de conversión:")
    print("1. Temperatura")
    print("2. Masa")
    print("3. Tiempo")
    
    opcion = int(input("Ingresa el número de la opción: "))
    
    if opcion == 1:
        manejar_temperatura()
    elif opcion == 2:
        manejar_masa()
    elif opcion == 3:
        manejar_tiempo()
    else:
        print("Opción no válida")

def manejar_temperatura():
    valor = float(input("Ingresa el valor de la temperatura: "))
    unidad_origen = input("Ingresa la unidad de origen (Celsius/Fahrenheit/Kelvin): ").lower()
    unidad_destino = input("Ingresa la unidad de destino (Celsius/Fahrenheit/Kelvin): ").lower()
    
    if unidad_origen == "celsius" and unidad_destino == "fahrenheit":
        print(temperatura.celsius_a_fahrenheit(valor))
    # Añade más conversiones de temperatura según sea necesario.

def manejar_masa():
    valor = float(input("Ingresa el valor de la masa: "))
    unidad_origen = input("Ingresa la unidad de origen (kg/g/t): ").lower()
    unidad_destino = input("Ingresa la unidad de destino (kg/g/t): ").lower()
    
    if unidad_origen == "kg" and unidad_destino == "g":
        print(masa.kilogramos_a_gramos(valor))
    # Añade más conversiones de masa según sea necesario.

def manejar_tiempo():
    valor = float(input("Ingresa el valor del tiempo: "))
    unidad_origen = input("Ingresa la unidad de origen (segundos/minutos/horas): ").lower()
    unidad_destino = input("Ingresa la unidad de destino (segundos/minutos/horas): ").lower()
    
    if unidad_origen == "segundos" and unidad_destino == "minutos":
        print(tiempo.segundos_a_minutos(valor))
    # Añade más conversiones de tiempo según sea necesario.

if __name__ == "__main__":
    menu()
