# Utilty Classes

A list of Utility Classes you can use in your programs.

---

# Additel.py

## Additel

Can be imported by using something like:
```python
import Utility.Additel from Additel
```

#### Additel.getUnits()

| Static Function | returns AdditelUnit [] | Gets a list of serial settings for Additel Units.  Will ignore any serial ports currently in use. |

#### Constants

| Name | Value |
| --- | ---|
| Additel.ADT220 | "ADT220" |
| Additel.ADT221A | "ADT221A" |
| Additel.ADT222A | "ADT222A" |
| Additel.ADT223A | "ADT223A" |
| Additel.ADT672 | "ADT672 |
| Additel.ADT681 | "ADT681" |
| Additel.ADT761 | "ADT761" |
| Additel.UNKNOWN_UNIT | "UNKNOWN_UNIT" |

## AdditelUnit

[Additel.getUnits()](#additel) returns an array of these.

Properties:

| Name | Type / Value | Description |
| --- | --- | --- |
| port | String | The port address the unit is communicating from (In Windows it is COM1, COM2, etc.  In Mac or Linux it is /dev/tty.________). |
| baudrate | 2400, 4800, 9600, 19200, 38400, 57600, 115200 | The baud rate at which the device is communicating at. |
| databits | serial.EIGHTBITS, serial.SEVENBITS | The number of bits used to send data between the unit and computer. |
| parity | serial.PARITY_NONE | The parity of the unit.  For Additel units, the value is always None. |
| stopbits | serial.STOPBITS_ONE, serial.STOPBITS_TWO | The number of bits used to signal the end of a piece of data sent between the unit and comptuer. |
| unit | Additel.ADT220, Additel.ADT221A, Additel.ADT222A, Additel.ADT223A, Additel.ADT672, Additel.ADT681, Additel.ADT761, Additel.UNKNOWN_UNIT | The type of unit at that serial port, as a constant.  The constants are strings. |