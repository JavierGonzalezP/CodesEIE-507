import serial

puerto_serie = '/dev/ttyUSB0'  # Puerto USB del Arduino
baud_rate = 9600  # Seteo de baudios

# Iniciar la comunicación serial con el Arduino
try:
    arduino = serial.Serial(puerto_serie, baud_rate)
    print(f'Conexion con Arduino en {puerto_serie} estable a {baud_rate} baudios.\n')
except serial.SerialException as e:
    print(f'Error al conectar con Arduino: {e}')
    exit()
    
try:
    while True:
        # Leer datos desde el Arduino
        datos = arduino.readline().decode('utf-8').strip()
        if datos:
            print(f'{datos}')
            
except KeyboardInterrupt:
    print('Comunicacion serial interrumpida')
    
finally:
    arduino.close()
    