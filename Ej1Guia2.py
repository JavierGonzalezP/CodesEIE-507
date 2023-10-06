import serial
import time

class ComunicacionSerial:
    def __init__(self, puerto, baudios):
        self.puerto = puerto
        self.baudios = baudios
        self.serial_connection = None
    def abrir_conexion(self):
        try:
            self.serial_connection = serial.Serial(self.puerto, self.baudios, timeout=1)
            print(f"Conexión serial abierta en {self.puerto} a {self.baudios} bps")
        except serial.SerialException:
            print(f"No se pudo abrir la conexión serial en {self.puerto}")
    def cerrar_conexion(self):
        if self.serial_connection:
            self.serial_connection.close()
            print("Conexión serial cerrada")
    def read_data(self):
        if self.serial_connection:
            data = self.serial_connection.readline().decode().strip()
            return data

if __name__ == "__main__":
    # Definir el puerto y la velocidad de comunicación del Arduino
    arduino_puerto = "/dev/ttyUSB0"
    baudios = 9600
    # Crear una instancia de la clase ComunicacionSerial
    serial_comm = ComunicacionSerial(arduino_puerto, baudios)
    try:
        serial_comm.abrir_conexion()
        while True:
            # Leer datos del Arduino
            received_data = serial_comm.read_data()
            if received_data:
                print(f"Recibido: {received_data}")
            time.sleep(0.1)
    except KeyboardInterrupt:
        pass
    finally:
        # Cerrar la conexión serial al finalizar
        serial_comm.cerrar_conexion()


