"A class used to perform typical utility actions with Additel units."

#import serial and the serial enumeration tool
import serial
import serial.tools.list_ports

#import threading so we can make things a tiny bit faster
import threading

class AdditelUnit:
    "Acts as a Struct to store valid serial information of an Additel Unit"
    def __init__(self, port, baudRate, dataBit, parity, stopBit):
        self.port = port
        self.baudRate = baudRate
        self.dataBit = dataBit
        self.parity = parity
        self.stopBit = stopBit

class testPort(threading.Thread):
    "A class used for threading, simply to run a function to test a certain port"
    def __init__(self, port):
        threading.Thread.__init__(self)
        self.port = port

    def run(self):
        # we start with 9600 because that's the default baud rate
        baudRates = [9600, 2400, 4800, 19200, 38400, 57600, 115200]
        # possibilities for data bits and stop bits
        dataBits = [serial.EIGHTBITS, serial.SEVENBITS]
        stopBits = [serial.STOPBITS_ONE, serial.STOPBITS_TWO]

        # iterate through each combination of baud rates, data bits, and stop bits
        for baudRate in baudRates:
            for dataBit in dataBits:
                for stopBit in stopBits:

                    # open a port with the specified settings and write to it
                    # set the timeout rate to a small number
                    # because we will pull for possible output multiple times
                    try:
                        open_port = serial.Serial(self.port, baudRate, dataBit, serial.PARITY_NONE, stopBit, 0.01)
                        open_port.write("255:R:OTEST:1\r\n")

                        # we will pull for data 10 times
                        for x in range(0,10):
                            output = open_port.read(size=1)

                            #if there is any data
                            if (len(output) != 0):

                                # append the unit to the list of units in a threadsafe manner
                                try:
                                    Additel.unitsLock.acquire()
                                    foundUnit = AdditelUnit(self.port, baudRate, dataBit, serial.PARITY_NONE, stopBit)
                                    Additel.units.append(foundUnit)
                                finally:
                                    Additel.unitsLock.release()

                                #close the port and quit the function (exiting the thread too)
                                open_port.close()
                                return
                        
                        # if we weren't able to find anything, close the port
                        open_port.close()
                    except ValueError:
                        pass

class Additel:
    "A class used to perform typical utility actions with Additel units."
    # create a units list and a lock to keep it threadsafe
    units = []
    unitsLock = threading.Lock()

    # create a lock to make getUnits only callable once at a time
    getUnitsLock = threading.Lock()
    
    @staticmethod
    def getUnits():
        "Gets a list of serial settings for Additel Units.  Will ignore any serial ports currently in use."
        # lock the function to make sure we don't have concurrent calls modifying the same class variables
        Additel.getUnitsLock.acquire()

        # get a list of available ports to communicate with
        ports = list(serial.tools.list_ports.comports())

        # keep a list of threads
        threads = []

        # for each port, create a thread that tests that port
        for port in ports:
            thread = testPort(port.device)
            thread.start()
            threads.append(thread)

        # wait until all the threads are done
        for thread in threads:
            thread.join()

        # copy our units and empty the original list
        unitsCopy = list(Additel.units)
        Additel.units = []

        # release our hold on this function
        Additel.getUnitsLock.release()

        # return the copy of teh list
        return list(unitsCopy)