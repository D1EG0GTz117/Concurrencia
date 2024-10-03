import threading

# Lista para almacenar resultados parciales
resultados = [0, 0]

# Función para calcular la suma de un rango y almacenar el resultado
def sumar_rango(inicio, fin, indice):
    suma_parcial = sum(range(inicio, fin + 1))
    resultados[indice] = suma_parcial

if __name__ == "__main__":
    numero_maximo = 10
    mitad = numero_maximo // 2

    # Crear dos hilos, uno para cada mitad del rango
    hilo_parte1 = threading.Thread(target=sumar_rango, args=(1, mitad, 0))
    hilo_parte2 = threading.Thread(target=sumar_rango, args=(mitad + 1, numero_maximo, 1))

    # Iniciar los hilos
    hilo_parte1.start()
    hilo_parte2.start()

    # Esperar a que ambos hilos terminen
    hilo_parte1.join()
    hilo_parte2.join()

    # Sumar los resultados parciales
    suma_total = resultados[0] + resultados[1]
    print(f"La suma total es: {suma_total}")
