import serial.tools.list_ports
ports = list(serial.tools.list_ports.comports())
units = []
for port in ports:
    print port.device
    open_port = serial.Serial(port.device, 9600, serial.EIGHTBITS, serial.PARITY_NONE, serial.STOPBITS_ONE, 1)
    open_port.close()