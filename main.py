# TODO: -add time polling for sensor read timestamps (tpoll.py)
#       -add data packing (temp + hum + timestamps) for LoRa
#       -add LoRa data transmission FiPy-1
#       -add LoRa data reception FiPy-2
#       -add data packing for WiFi
#       -add WiFi data transmision to server

# LED Color constants and meaning
ON = 0xFFFFFF
OFF = 0x000000
RED = 0xFF0000 # Invalid Transmission
GREEN = 0x00FF00 # Valid Transmission
BLUE = 0x0000FF # Valid Sensor Read
ORANGE = 0xFFA500 # Invalid Sensor Read

# LED start-up routine
pycom.rgbled(ON)
time.sleep_ms(200)
pycom.rgbled(OFF)
time.sleep_ms(50)
pycom.rgbled(GREEN)
time.sleep_ms(200)
pycom.rgbled(OFF)
time.sleep_ms(50)
pycom.rgbled(ON)
time.sleep_ms(200)
pycom.rgbled(OFF)
time.sleep_ms(100)

while True:
    # Sensor Read
    result = th.read()
    if result.is_valid():
        pycom.rgbled(BLUE)
        print("\nTemperature: %d C" % result.temperature)
        print("Humidity: %d %%" % result.humidity)
    else:
        pycom.rgbled(ORANGE)
        print("\nInvalid sensor read result.")
    time.sleep_ms(500)
    pycom.rgbled(OFF) # turn OFF LED
    time.sleep(1)

    # Poll time block {...}
    # Pack data for LoRa transmission block {...}
    # LoRa data trasmission block {...}
