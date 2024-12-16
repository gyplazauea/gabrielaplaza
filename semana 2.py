from abc import ABC, abstractmethod

# Abstracción: Definimos una clase abstracta
class Animal(ABC):
    def __init__(self, nombre):
        self.__nombre = nombre  # Encapsulación: Atributo privado

    @abstractmethod
    def hacer_sonido(self):
        pass

    def get_nombre(self):  # Encapsulación: Método para acceder al atributo privado
        return self.__nombre

# Herencia: Clases que extienden de Animal
class Perro(Animal):
    def __init__(self, nombre, raza):
        super().__init__(nombre)
        self.raza = raza

    def hacer_sonido(self):  # Polimorfismo: Implementación específica
        return "Guau guau"

class Gato(Animal):
    def __init__(self, nombre, color):
        super().__init__(nombre)
        self.color = color

    def hacer_sonido(self):  # Polimorfismo: Implementación específica
        return "Miau miau"

class Vaca(Animal):
    def hacer_sonido(self):  # Polimorfismo: Implementación específica
        return "Muuu"

# Uso del programa
if __name__ == "__main__":
    # Creación de objetos
    perro = Perro("Max", "Golden Retriever")
    gato = Gato("Luna", "Negro")
    vaca = Vaca("Molly")

    # Lista de animales
    animales = [perro, gato, vaca]

    # Iteramos mostrando los sonidos (polimorfismo) y el nombre (encapsulación)
    for animal in animales:
        print(f"{animal.get_nombre()} dice: {animal.hacer_sonido()}")

    # Ejemplo de acceso a atributos específicos por herencia
    print(f"{perro.get_nombre()} es un {perro.raza}.")
    print(f"{gato.get_nombre()} tiene un pelaje de color {gato.color}.")


