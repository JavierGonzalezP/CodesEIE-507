import random
import time
from datetime import datetime

class AdquisicionDatosTemperatura:
    def __init__(self):
        self.temperaturas = []
        self.inicio_tiempo = time.time()
    def generar_temperatura(self):
        temperatura = round(random.uniform(20, 30), 2)  # Simular temperatura entre 20°C y 30°C
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.temperaturas.append((timestamp, temperatura))
        print(f"Timestamp: {timestamp}, Temperatura: {temperatura}°C")
    def registrar_temperatura_promedio(self):
        tiempo_actual = time.time()
        if tiempo_actual - self.inicio_tiempo >= 300:  # 5 minutos (300 segundos)
            if self.temperaturas:
                temperatura_promedio = round(sum(temp[1] for temp in self.temperaturas) / len(self.temperaturas), 2)
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                with open("registro_temperatura.txt", "a") as archivo:
                    archivo.write(f"Timestamp: {timestamp}, Temperatura Promedio: {temperatura_promedio}°C\n")
                print(f"Timestamp: {timestamp}, Temperatura Promedio: {temperatura_promedio}°C (Registrada)")
                self.temperaturas = []  # Reiniciar la lista de temperaturas
                self.inicio_tiempo = tiempo_actual  # Reiniciar el tiempo de inicio
    def ejecutar(self):
        while True:
            self.generar_temperatura()
            self.registrar_temperatura_promedio()
            time.sleep(30)  # Esperar 30 segundos antes de generar el siguiente dato

if __name__ == "__main__":
    adquisicion_datos = AdquisicionDatosTemperatura()
    adquisicion_datos.ejecutar()


