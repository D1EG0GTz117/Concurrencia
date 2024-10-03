from multiprocessing import Process, Value

# Función para calcular la suma en un proceso separado
def calcular_suma(n, resultado):
    suma_total = sum(range(1, n + 1))
    resultado.value = suma_total

if __name__ == '__main__':
    n = 100000
    resultado = Value('i', 0)  # Compartir el valor entre procesos (entero inicializado en 0)

    # Crear un proceso para calcular la suma
    proceso = Process(target=calcular_suma, args=(n, resultado))

    # Iniciar el proceso
    proceso.start()

    # Esperar a que el proceso termine
    proceso.join()

    # Mostrar el resultado
    print(f"La suma total es: {resultado.value}")
