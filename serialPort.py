import sys
import serial


PortName = 'COM1'
ser = serial.Serial(PortName, timeout=2)

print ser.name
print ser.port

command = raw_input("user command: ")
ser.write("255:R:"+command+":1\r\n")
print ser.read(size=500)
