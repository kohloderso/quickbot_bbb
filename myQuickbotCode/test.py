import quickbot_config as config
import Adafruit_BBIO.ADC as ADC
import Adafruit_BBIO.PWM as PWM
import Adafruit_BBIO.GPIO as GPIO

LEFT = 0
RIGHT = 1
MIN = 0
MAX = 1

# Motor Pins -- (LEFT, RIGHT)
dir1Pin = (config.INl1, config.INr1)
dir2Pin = (config.INl2, config.INr2)
pwmPin = (config.PWMl, config.PWMr)

"""Initialize GPIO pins"""
GPIO.setup(dir1Pin[LEFT], GPIO.OUT)
GPIO.setup(dir2Pin[LEFT], GPIO.OUT)
GPIO.setup(dir1Pin[RIGHT], GPIO.OUT)
GPIO.setup(dir2Pin[RIGHT], GPIO.OUT)

PWM.start(pwmPin[LEFT], 0)#, frequency=frequency)
PWM.start(pwmPin[RIGHT], 0)#, frequency=frequency)

"""left motor forward?"""
GPIO.output(dir1Pin[LEFT], GPIO.LOW)
GPIO.output(dir2Pin[LEFT], GPIO.HIGH)
PWM.set_duty_cycle(pwmPin[LEFT], 100)

PWM.stop(pwmPin[LEFT])
PWM.stop(pwmPin[RIGHT])
PWM.cleanup()