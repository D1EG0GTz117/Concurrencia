import time
import threading

class Temporizador:
    def __init__(self, duracion: int) -> None:
        self.duracion = duracion

    def iniciar_pausa(self) -> None:
        print("Inicio de la pausa...")
        time.sleep(self.duracion)
        print("Fin de la pausa.")

def iniciar_pausa_en_hilo(duracion: int) -> None:
    temporizador = Temporizador(duracion)
    hilo = threading.Thread(target=temporizador.iniciar_pausa)
    hilo.start()


iniciar_pausa_en_hilo(5)
