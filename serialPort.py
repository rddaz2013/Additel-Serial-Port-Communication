# import the pyserial library
import serial

# open a serial port
port = serial.Serial(   port='COM3',
                        baudrate=9600,
                        bytesize=serial.EIGHTBITS,
                        parity=serial.PARITY_NONE,
                        stopbits=serial.STOPBITS_ONE,
                        timeout=1   )

# write the OTEST command to the serial port
# if you have an ADT761, use "255:R:ODEVSN:1\r\n" instead
port.write("255:W:OFSAP:1\r\n")

# read the first 500 characters (or less if it has a quicker timeout)
for x in range(1,100):
    print port.read(size=500)