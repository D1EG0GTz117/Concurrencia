class CalculoInteres:
    def __init__(self) -> None:
        self.monto_inicial = self.obtener_monto_inicial()
        self.porcentaje_tasa = self.obtener_porcentaje_tasa()
        self.duracion = self.obtener_duracion()
        self.interes_generado = self.calcular_interes()

    def obtener_monto_inicial(self) -> float:
        return float(input("Introduce el capital inicial:"))

    def obtener_porcentaje_tasa(self) -> float:
        return float(input("Introduce la tasa de interés anual (en porcentaje):")) / 100

    def obtener_duracion(self) -> float:
        return float(input("Introduce el tiempo en años:"))

    def calcular_interes(self) -> float:
        return self.monto_inicial * self.porcentaje_tasa * self.duracion

    def mostrar_resultado(self) -> None:
        print(f"Capital inicial: {self.monto_inicial:.2f}")
        print(f"Tasa de interés anual: {self.porcentaje_tasa * 100:.2f}%")
        print(f"Duración: {self.duracion} años")
        print(f"Interés generado: {self.interes_generado:.2f}")


interes = CalculoInteres()
interes.mostrar_resultado()
