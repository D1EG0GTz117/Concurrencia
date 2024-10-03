class Persona:
    def __init__(self) -> None:
        self.nombre = ""
        self.edad = 0
        self.ingresar_datos()

    def ingresar_datos(self) -> None:
        self.nombre = input("Ingresa tu nombre: ")
        self.edad = self.ingresar_edad()

    def ingresar_edad(self) -> int:
        while True:
            try:
                edad = int(input("Ingresa tu edad: "))
                if edad < 0:
                    raise ValueError("La edad no puede ser negativa.")
                return edad
            except ValueError as e:
                print(f"Entrada inválida: {e}. Por favor, ingresa un número entero positivo.")

    def imprimir_datos(self) -> None:
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")


persona = Persona()
persona.imprimir_datos()
