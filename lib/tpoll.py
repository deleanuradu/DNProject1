# Library for RTC sync 

from machine import RTC
import time
import pycom
import socket
import utime
import machine

def setRTCLocalTime():
    rtc = machine.RTC()
    rtc.ntp_sync("pool.ntp.org") # poll ntp server
    utime.sleep_ms(750)
    print('\nRTC Set from NTP to UTC:', rtc.now())
    utime.timezone(-18000)
    print('Adjusted from UTC to EST timezone', utime.localtime(), '\n') # update to local time
