import Adafruit_BBIO.ADC as ADC
import time


ADC.setup()
sensor1 = "P9_40" 	# left infrared sensor
sensor2 = "P9_39"	
sensor3 = "P9_38"	# middle infrared sensor
sensor4 = "P9_37"
sensor5 = "P9_36"	# right infrared sensor


while True:
    #reading1 = ADC.read(sensor1)
    #reading2 = ADC.read(sensor2)
    #reading3 = ADC.read(sensor3)
    #reading4 = ADC.read(sensor4)
    #reading5 = ADC.read(sensor5)
    #print("reading2 " + str(reading2))
    print("reading3 " + str(reading3))
    time.sleep(0.05)
