import quickbot_config as config
import Adafruit_BBIO.ADC as ADC
import Adafruit_BBIO.PWM as PWM
import Adafruit_BBIO.GPIO as GPIO
import time

ADC.setup()
while True:
    value_l = ADC.read(config.Ol)
    value_r = ADC.read(config.Or)

    print("left: " + string(value_l) + "right: " + string(value_r))