import time
import threading

class TemporizadorRegresivo:
    def __init__(self) -> None:
        self.duracion = 0

    def iniciar_cuenta_regresiva(self, segundos: int) -> None:
        self.duracion = segundos
        for i in range(self.duracion, -1, -1):
            print(f"Tiempo restante: {i:02} segundos", end="\r")
            time.sleep(1)
        print("\n¡Despegue!")

def iniciar_hilo_cuenta_regresiva() -> None: 
    cuenta_regresiva = TemporizadorRegresivo()
    hilo = threading.Thread(target=cuenta_regresiva.iniciar_cuenta_regresiva, args=(10,))
    hilo.start()

iniciar_hilo_cuenta_regresiva()
