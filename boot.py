import pycom
import time
from machine import Pin
from dth import DTH

pycom.heartbeat(False) # turn off heartbeat LED
th = DTH('P3',0) # Assign 'P3' as input pin or sensor read

print("\n*** FiPy-1 successfully booted! ***\n")
