import time
import threading

class Temporizador:
    def __init__(self) -> None:
        self.milisegundos = 0
        self.segundos = 0
        self.minutos = 0
        self.horas = 0

    def iniciar_temporizador(self) -> None:
        while True:
            self.actualizar_tiempo()
            time.sleep(0.1)  # Esperar 0.1 segundos antes de actualizar

    def actualizar_tiempo(self) -> None:
        print(f"{self.horas:02}:{self.minutos:02}:{self.segundos:02}:{self.milisegundos:02}", end="\r")
        self.milisegundos += 1
        
        if self.milisegundos >= 10:
            self.milisegundos = 0
            self.segundos += 1
            
            if self.segundos >= 60:
                self.segundos = 0
                self.minutos += 1
                
                if self.minutos >= 60:
                    self.minutos = 0
                    self.horas += 1

def iniciar_contador_en_hilo():
    temporizador = Temporizador()
    hilo = threading.Thread(target=temporizador.iniciar_temporizador, daemon=True)
    hilo.start()


iniciar_contador_en_hilo()


try:
    while True:
        time.sleep(1)  
except KeyboardInterrupt:
    print("\nTemporizador detenido.")
