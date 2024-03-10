
import threading
import time
import random

# Función que será ejecutada por cada hilo
def descarga_juegos(juego):
    tiempo_descarga = random.randint(1, 5)
    print(f"Descargando juego {juego}. Tiempo estimado: {tiempo_descarga} segundos.")
    time.sleep(tiempo_descarga)
    print(f"{juego} descargado exitosamente en {tiempo_descarga} segundos.")

# Lista de juegos a descargar
juegos_a_descargar = ["minecraft", "codm", "gears 3", "fortnite", "resident evil", "fall guys","Megaman"]

# Crear un contador de tiempo para asegurar que el tercer juego se ejecute después de 10 segundos
contador_tiempo = 0

hilos = []
for juego in juegos_a_descargar:
    # Introduce un retraso de 10 segundos antes de iniciar la descarga del tercer juego
    if juego == "gears 3":
        time.sleep(10)
        contador_tiempo += 10
    hilo = threading.Thread(target=descarga_juegos, args=(juego,))
    hilos.append(hilo)
    hilo.start()

# Espera a que todos los hilos finalicen
for hilo in hilos:
    hilo.join()

print("Todos los juegos han sido descargados.")
