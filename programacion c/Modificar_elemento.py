class ListaColores:
    def __init__(self) -> None:
        self.colores = ["rojo", "verde", "azul", "amarillo"]

    def cambiar_color(self) -> None:
        self.mostrar_colores()
        indice = int(input("Ingresa el índice del color a cambiar: "))
        
        if 0 <= indice < len(self.colores):
            nuevo_color = input("Ingresa el nuevo color: ")
            self.colores[indice] = nuevo_color
            print("Color cambiado con éxito.")
        else:
            print("Índice inválido. Por favor, inténtalo de nuevo.")

    def mostrar_colores(self) -> None:
        print(f"Colores actuales: {self.colores}")


lista_colores = ListaColores()
lista_colores.cambiar_color()
lista_colores.mostrar_colores()
