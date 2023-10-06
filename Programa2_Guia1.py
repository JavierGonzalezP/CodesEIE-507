import spidev

def setup_spi():
    spi_bus = 0
    spi_device = 0
    spi = spidev.SpiDev()
    spi.open(spi_bus, spi_device)
    spi.max_speed_hz = 1000000
    return spi

def read_data_from_arduino(spi):
    send_byte = 0x80
    rcv_byte = spi.xfer2([send_byte])
    rcv_byte = spi.xfer2([send_byte])
    data_recv = rcv_byte[0]
    return data_recv

def main():
    spi = setup_spi()
    data_recv = read_data_from_arduino(spi)
    if data_recv != 0x80:
        print("Datos Recibidos Arduino: " + str(data_recv))
    else:
        print("No se recibieron datos válidos desde Arduino")

    spi.close()

if name == "main":
    main()