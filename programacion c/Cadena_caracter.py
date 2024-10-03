class ContadorCaracteres:
    def __init__(self) -> None:
        self.texto = self.solicitar_texto()
        self.letra = self.solicitar_letra()

    def solicitar_texto(self) -> str:
        return input("ingresa un texto:")

    def solicitar_letra(self) -> str:
        while True:
            letra = input("ingresa una letra a contar:")
            if len(letra) == 1:
                return letra
            else:
                print("Debes ingresar solo un carácter.")

    def mostrar_conteo(self) -> None:
        conteo = self.texto.count(self.letra)
        print(f"El carácter '{self.letra}' aparece {conteo} veces en el texto.")


contador = ContadorCaracteres()
contador.mostrar_conteo()
