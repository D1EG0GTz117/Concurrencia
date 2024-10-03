import threading

class CalculoInteresSimple:
    def __init__(self) -> None:
        self.capital = 0.0
        self.tasa = 0.0
        self.tiempo = 0.0
        self.interes = 0.0

    def asignar_valores(self) -> None:
        self.capital = float(input("Introduce el capital: "))
        self.tasa = float(input("Introduce la tasa de interés anual (como decimal): "))
        self.tiempo = float(input("Introduce el tiempo en años: "))

    def calcular_interes(self) -> None:
        self.interes = self.capital * self.tasa * self.tiempo

    def mostrar_resultado(self) -> None:
        print(f"Capital: {self.capital}")
        print(f"Tasa de interés anual: {self.tasa * 100}%")
        print(f"Tiempo: {self.tiempo} años")
        print(f"Interés acumulado: {self.interes}")

    def ejecutar(self) -> None:
        self.asignar_valores()
        self.calcular_interes()
        self.mostrar_resultado()


def iniciar_calculo_en_hilo():
    interes_simple = CalculoInteresSimple()
    hilo = threading.Thread(target=interes_simple.ejecutar)
    hilo.start()


iniciar_calculo_en_hilo()
