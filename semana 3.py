# ================================
# Programación Tradicional
# ================================

# Función para ingresar temperaturas diarias
def ingresar_temperaturas():
    temperaturas = []
    print("Ingresa la temperatura diaria para 7 días:")
    for i in range(7):
        temp = float(input(f"Día {i + 1}: "))
        temperaturas.append(temp)
    return temperaturas

# Función para calcular el promedio semanal
def calcular_promedio(temperaturas):
    return sum(temperaturas) / len(temperaturas)

# Función principal para ejecutar el programa Tradicional
def programa_tradicional():
    print("Programa Tradicional: Promedio Semanal del Clima")
    temperaturas = ingresar_temperaturas()
    promedio = calcular_promedio(temperaturas)
    print(f"\nEl promedio semanal del clima es: {promedio:.2f}°C")


# ================================
# Programación Orientada a Objetos (POO)
# ================================

class ClimaSemanal:
    def __init__(self):
        self.__temperaturas = []  # Encapsulación: atributo privado para almacenar temperaturas

    def ingresar_temperaturas(self):
        print("Ingresa la temperatura diaria para 7 días:")
        for i in range(7):
            temp = float(input(f"Día {i + 1}: "))
            self.__temperaturas.append(temp)

    def calcular_promedio(self):
        if len(self.__temperaturas) == 0:
            print("No se han ingresado temperaturas.")
            return 0
        return sum(self.__temperaturas) / len(self.__temperaturas)

    def mostrar_promedio(self):
        promedio = self.calcular_promedio()
        print(f"\nEl promedio semanal del clima es: {promedio:.2f}°C")

    # Método getter para obtener las temperaturas
    def obtener_temperaturas(self):
        return self.__temperaturas

# Clase derivada para una demostración de herencia
class ClimaDetallado(ClimaSemanal):
    def mostrar_temperaturas(self):
        # Ahora usamos el método getter para obtener las temperaturas
        temperaturas = self.obtener_temperaturas()
        print("\nTemperaturas diarias ingresadas:")
        for i, temp in enumerate(temperaturas, 1):
            print(f"Día {i}: {temp}°C")

# ================================
# Ejecución del Programa
# ================================

def main():
    # Selección de modo de ejecución
    print("Selecciona el tipo de implementación:")
    print("1. Programación Tradicional")
    print("2. Programación Orientada a Objetos (POO)")
    seleccion = int(input("Ingresa tu elección (1 o 2): "))

    if seleccion == 1:
        programa_tradicional()  # Llamamos a la función correcta
    elif seleccion == 2:
        clima = ClimaDetallado()
        clima.ingresar_temperaturas()
        clima.mostrar_temperaturas()
        clima.mostrar_promedio()
    else:
        print("Opción no válida.")

# Ejecución del programa principal
if __name__ == "__main__":
    main()

