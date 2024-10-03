import threading

class Fruta:
    def __init__(self, frutas=None) -> None:
        if frutas is None:
            frutas = ["🍎", "🍉", "🥭", "🍑"]
        self.frutas = frutas
        self.indice = self.asignar_indice()
        
    def asignar_indice(self) -> int:
        while True:
            try:
                indice = int(input("Ingresa un índice (0-3):"))
                if 0 <= indice < len(self.frutas):
                    return indice
                else:
                    print("Índice fuera de rango. Intenta de nuevo.")
            except ValueError:
                print("Entrada inválida. Por favor ingresa un número.")

    def imprimir_lista(self) -> None:
        print(f"El elemento en el indice {self.indice} es: {self.frutas[self.indice]}")

frutalista = Fruta()


hilo = threading.Thread(target=frutalista.imprimir_lista, daemon=True)
hilo.start()


hilo.join()