# Utilty Classes

A list of Utility Classes you can use in your programs.

---
# Additel

Can be imported by using something like:
```python
import Utility.Additel from Additel
```

### Additel.getUnits()

*Static Function.  Gets a list of serial settings for Additel Units.  Will ignore any serial ports currently in use.*

**returns AdditelUnit []**

### Constants

| Name | Value |
| --- | ---|
| **Additel.ADT220** | "ADT220" |
| **Additel.ADT221A** | "ADT221A" |
| **Additel.ADT222A** | "ADT222A" |
| **Additel.ADT223A** | "ADT223A" |
| **Additel.ADT672** | "ADT672 |
| **Additel.ADT681** | "ADT681" |
| **Additel.ADT761** | "ADT761" |
| **Additel.UNKNOWN_UNIT** | "UNKNOWN_UNIT" |

# AdditelUnit

[Additel.getUnits()](#additel) returns an array of these.

### Properties:

| Name | Type / Value | Description |
| --- | --- | --- |
| **port** | String | The port address.  In Windows, COM1, COM2, etc.  In Mac or Linux, /dev/tty.________. |
| **baudrate** | *Number* - 2400, 4800, 9600, 19200, 38400, 57600, 115200 | The baud rate frequency. |
| **databits** | *Constant* - serial.EIGHTBITS, serial.SEVENBITS | The number of bits used to send data. |
| **parity** | *Constant* - serial.PARITY_NONE | The parity of the unit (for Additel units, always NONE) |
| **stopbits** | *Constant* - serial.STOPBITS_ONE, serial.STOPBITS_TWO | The number of bits used to signal the end of a packet. |
| **unit** | *Constant* - Additel.ADT220, Additel.ADT221A, Additel.ADT222A, Additel.ADT223A, Additel.ADT672, Additel.ADT681, Additel.ADT761, Additel.UNKNOWN_UNIT | The Additel unit at the serial port. |
