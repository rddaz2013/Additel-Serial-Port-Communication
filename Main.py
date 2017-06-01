import serial.tools.list_ports
ports = list(serial.tools.list_ports.comports())
for p in ports:
    print p
var = raw_input("Pres Enter to continue: ")