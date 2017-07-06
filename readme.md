Welcome to the Additel Serial Port Communcation repository.

Here you can find examples and a few utility classes for working with Additel units.

<<<<<<< HEAD
## Prerequisites

These examples and utilites are written mostly in Python, though you may sees a few written in other languages.  To get these to compile and run, you will need:

#### [Python 2 for Windows](https://www.python.org/downloads/ "Python 2 for Windows")
Our examples use Python 2, though there is a chance that much of it will work with Python 3 as well.  The classes should be easy enough to read through and change, so if you do need to alter them, they shouldn't be too hard to work with.

#### [pySerial](http://pythonhosted.org/pyserial/pyserial.html#installation "pySerial")
=======
##Prerequisites

These examples and utilites are written mostly in Python, though you may sees a few written in other languages.  To get these to compile and run, you will need:

####[Python 2 for Windows](https://www.python.org/downloads/ "Python 2 for Windows")
Our examples use Python 2, though there is a chance that much of it will work with Python 3 as well.  The classes should be easy enough to read through and change, so if you do need to alter them, they shouldn't be too hard to work with.

####[pySerial](http://pythonhosted.org/pyserial/pyserial.html#installation "pySerial")
>>>>>>> 0c9378065fd0c53661dd7bd62cfc9e7a438a3377
This is a cross platform python library that makes working with serial ports very easy.  I wish all languages had a serial library like this!  You can install this either using PyPI or directly.

And that should be it.  If you are coming from another language, I also highly reccomend that you [add Python to your Path Enviromental Variable](https://stackoverflow.com/questions/3701646/how-to-add-to-the-pythonpath-in-windows-7 "Stack Overflow").  I used Bamara Coulibaly's answer.  But I'm guessing the higher voted answers work even better.

---

This repository contains basic information, utilities, and examples of how to communicate with Additel Pressure and Electrical Units via RS232 Serial Commands.

We are currently revamping it a bit to have a tutorial and other details to make communicating with a serial port easier.

Here is a small introduction to programming for these units:
https://docs.google.com/document/d/10mg2ai0xhQEOzkcn_KFtL0X6zdXY_TRhn_qwrkdjd-U/pub