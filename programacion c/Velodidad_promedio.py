class PromedioVelocidad:
    def __init__(self) -> None:
        self.distancia_recorrida = self.obtener_distancia()
        self.tiempo_empleado = self.obtener_tiempo()
        self.velocidad_promedio = self.calcular_velocidad()

    def obtener_distancia(self) -> float:
        return float(input("Introduce la distancia recorrida en kilómetros:"))

    def obtener_tiempo(self) -> float:
        return float(input("Introduce el tiempo empleado en horas:"))

    def calcular_velocidad(self) -> float:
        if self.tiempo_empleado == 0:
            return 0.0
        return self.distancia_recorrida / self.tiempo_empleado

    def mostrar_resultado(self) -> None:
        if self.velocidad_promedio == 0.0:
            print("El tiempo no puede ser cero.")
        else:
            print(f"Distancia: {self.distancia_recorrida:.2f} km")
            print(f"Tiempo: {self.tiempo_empleado:.2f} horas")
            print(f"La velocidad promedio es: {self.velocidad_promedio:.2f} km/h")


velocidad = PromedioVelocidad()
velocidad.mostrar_resultado()
