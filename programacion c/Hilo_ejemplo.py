import threading

class Persona:
    def __init__(self) -> None:
        self.nombre = ""
        self.edad = 0

    def ingresar_datos(self) -> None:
        self.nombre = input("Ingresa tu nombre: ")
        self.edad = int(input("Ingresa tu edad: "))

    def mostrar_datos(self) -> None:
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")

# Función que ejecuta el ingreso de datos en un hilo
def iniciar_ingreso_datos():
    persona = Persona()
    persona.ingresar_datos()
    persona.mostrar_datos()

# Iniciar el ingreso de datos en un hilo
hilo = threading.Thread(target=iniciar_ingreso_datos)
hilo.start()
