import quickbot_config as config
import Adafruit_BBIO.ADC as ADC
import Adafruit_BBIO.PWM as PWM
import Adafruit_BBIO.GPIO as GPIO
import time

ADC.setup()
while True:
    value_l = ADC.read(config.Ol)
    value_r = ADC.read(config.Or)

    print("left: " + str(value_l) + "right: " + str(value_r))
    time.sleep(1)