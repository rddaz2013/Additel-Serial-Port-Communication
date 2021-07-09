"

#import serial and the serial enumeration tool
import serial
import serial.tools.list_ports

#import threading so we can make things a tiny bit faster
import threading



class AdditelUnit:
    "Acts as a Struct to store valid serial information of an Additel Unit"

    def __init__(self, port, baudrate, databits, parity, stopbits, unit):
        self.port = port
        self.baudrate = baudrate
        self.databits = databits
        self.parity = parity
        self.stopbits = stopbits
        self.unit = unit



class testPort(threading.Thread):
    "A class used for threading, simply to run a function to test a certain port"

    def __init__(self, port):
        threading.Thread.__init__(self)
        self.port = port


    def __parse_unit_type(self, text, stopbits):
        "A function used to parse the unit type when given the response from 255:R:OTEST:1\r\n sliced to 13 characters"

        # get rid of the number and/or characters in front of the first colon
        text = text[text.find(":"):]

        # Additel 220 Unit
        if (text == ":F:OMODEL:Additel 220\0"):
            return Additel.ADT220

        # Additel 221A Unit
        elif (text == ":F:OMODEL:Additel 221A\0"):
            return Additel.ADT221A

        # Additel 222A Unit
        elif (text == ":F:OMODEL:Additel 222A\0"):
            return Additel.ADT222A

        # Additel 223A Unit
        elif (text == ":F:OMODEL:Additel 223A\0"):
            return Additel.ADT223A

        # Additel 672 Unit
        elif (text == ":E:OMODEL:1018\0"):
            return Additel.ADT672

        # Additel 681 Unit
        elif (text == ":E:OMODEL:1019\0"):
            return Additel.ADT681

        # Additel 761 Unit
        elif (text == ":E:OMODEL:1003\0"):
            return Additel.ADT761

        # None of the Above
        return Additel.UNKNOWN_UNIT


    def run(self):
        "The main function run by the threads.  Tests a port with different stop bits, data bits, and baud rates."

        # we start with 9600 because that's the default baud rate
        baudrate_list = [9600, 2400, 4800, 19200, 38400, 57600, 115200]

        # possibilities for data bits and stop bits
        databits_list = [serial.EIGHTBITS, serial.SEVENBITS]
        stopbits_list = [serial.STOPBITS_ONE, serial.STOPBITS_TWO]

        # iterate through each combination of baud rates, data bits, and stop bits
        for baudrate in baudrate_list:
            for databits in databits_list:
                for stopbits in stopbits_list:

                    # open a port with the specified settings and write to it
                    # set the timeout rate to a small number
                    # because we will pull for possible output multiple times
                    try:
                        open_port = serial.Serial(self.port, baudrate, databits, serial.PARITY_NONE, stopbits, 0.01)
                        open_port.write("255:R:OMODEL:1\r\n")

                        # we will pull for data 10 times
                        # (10 * 0.01 seconds each = 0.1 seconds total waiting time)
                        for x in range(0,10):
                            output = open_port.read(size=1)

                            #if there is any data
                            if (len(output) != 0):

                                # read all of the characters so we can make a decision on the unit type
                                more_output = " "
                                while (more_output != ""):
                                    more_output = open_port.read(size=1)
                                    output += more_output

                                #decide the unit type
                                unit_type = self.__parse_unit_type(output, stopbits)

                                # append the unit to the list of units in a threadsafe manner
                                try:
                                    Additel.unitsLock.acquire()
                                    found_unit = AdditelUnit(self.port, baudrate, databits, serial.PARITY_NONE, stopbits, unit_type)
                                    Additel.units.append(found_unit)
                                finally:
                                    Additel.unitsLock.release()

                                #close the port and quit the function (exiting the thread too)
                                open_port.close()
                                return
                        
                        # if we weren't able to find anything, close the port
                        open_port.close()

                    # For catching when the paramaters of serial.open are out of range
                    # But this should never happen
                    except ValueError:
                        pass



class Additel:
    "A class used to perform typical utility actions with Additel units."

    # create some constants to use with AdditelUnit objects
    ADT220 = "ADT220"
    ADT221A = "ADT221A"
    ADT222A = "ADT222A"
    ADT223A = "ADT223A"
    ADT672 = "ADT672"
    ADT681 = "ADT681"
    ADT761 = "ADT761"
    UNKNOWN_UNIT = "UNKNOWN_UNIT"
    
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
