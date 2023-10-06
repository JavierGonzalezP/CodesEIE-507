import smbus
from time import sleep

class MPU6050:
    def __init__(self, bus_num=1, direccion_dispositivo=0x68):
        self.bus = smbus.SMBus(bus_num)
        self.Direccion_Dispositivo = direccion_dispositivo
        # Definir registros del MPU6050
        self.PWR_MGMT_1 = 0x6B
        self.GYRO_CONFIG = 0x1B
        self.GYRO_XOUT_H = 0x43
        self.GYRO_YOUT_H = 0x45
        self.GYRO_ZOUT_H = 0x47
    def inicializar(self):
        self.bus.write_byte_data(self.Direccion_Dispositivo, self.PWR_MGMT_1, 1)
        self.bus.write_byte_data(self.Direccion_Dispositivo, self.GYRO_CONFIG, 24)
    def leer_datos(self, direccion):
        alto = self.bus.read_byte_data(self.Direccion_Dispositivo, direccion)
        bajo = self.bus.read_byte_data(self.Direccion_Dispositivo, direccion + 1)
        valor = ((alto << 8) | bajo)
        if valor > 32768:
            valor = valor - 65536
        return valor
    def leer_datos_giroscopio(self):
        gyro_x = self.leer_datos(self.GYRO_XOUT_H)
        gyro_y = self.leer_datos(self.GYRO_YOUT_H)
        gyro_z = self.leer_datos(self.GYRO_ZOUT_H)
        return gyro_x, gyro_y, gyro_z
    def convertir_datos_giroscopio(self, gyro_x, gyro_y, gyro_z):
        Gx = gyro_x / 131.0
        Gy = gyro_y / 131.0
        Gz = gyro_z / 131.0
        return Gx, Gy, Gz

if __name__ == "__main__":
    mpu = MPU6050()
    mpu.inicializar()
    print("Leyendo Datos del Giroscopio")
    while True:
        gyro_x, gyro_y, gyro_z = mpu.leer_datos_giroscopio()
        Gx, Gy, Gz = mpu.convertir_datos_giroscopio(gyro_x, gyro_y, gyro_z)
        print(f"Gx={Gx:.2f} °/s", f"Gy={Gy:.2f} °/s", f"Gz={Gz:.2f} °/s")
        sleep(1)


