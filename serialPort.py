# import the pyserial library
import serial

# open a serial port
port = serial.Serial(   port='COM3',
                        baudrate=9600,
                        bytesize=serial.EIGHTBITS,
                        parity=serial.PARITY_NONE,
                        stopbits=serial.STOPBITS_ONE,
                        timeout=1   )

# reads the SN of an ADT761
port.write("255:R:ODEVSN:1\r\n")

# read the first 500 characters (or less if it has a quicker timeout)
for _ in range(1,100):
    print(port.read(size=500))
