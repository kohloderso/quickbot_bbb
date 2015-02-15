import quickbot_config as config
import Adafruit_BBIO.ADC as ADC
import Adafruit_BBIO.PWM as PWM
import Adafruit_BBIO.GPIO as GPIO
import time

LEFT = 0
RIGHT = 1
MIN = 0
MAX = 1

ADC.setup()

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

# obstacle = False
# while not obstacle:
#     GPIO.output(dir1Pin[LEFT], GPIO.HIGH)
#     GPIO.output(dir2Pin[LEFT], GPIO.LOW)
#     PWM.set_duty_cycle(pwmPin[LEFT], 50)
#     GPIO.output(dir1Pin[RIGHT], GPIO.HIGH)
#     GPIO.output(dir2Pin[RIGHT], GPIO.LOW)
#     PWM.set_duty_cycle(pwmPin[RIGHT], 50)
#
#     reading1 = ADC.read(config.IRfl)
#     reading2 = ADC.read(config.IRfr)
#     reading3 = ADC.read(config.IRfm)
#     print("sensor left " + str(reading1))
#     print("sensor right " + str(reading2))
#     print("sensor middle " + str(reading3))
#
#     if max(reading1, reading2, reading3) > 0.5:
#         obstacle = True

middleIR = 0

while middleIR < 0.4:
    leftIR = ADC.read(config.IRfl)
    rightIR = ADC.read(config.IRfr)
    middleIR = ADC.read(config.IRfm)
    print("sensor left " + str(leftIR))
    print("sensor right " + str(rightIR))
    print("sensor middle " + str(middleIR))

    if leftIR > 0.2:
        GPIO.output(dir1Pin[LEFT], GPIO.HIGH)
        GPIO.output(dir2Pin[LEFT], GPIO.LOW)
        PWM.set_duty_cycle(pwmPin[LEFT], 50)
        PWM.set_duty_cycle(pwmPin[RIGHT], 0)
    elif rightIR > 0.2:
        GPIO.output(dir1Pin[RIGHT], GPIO.HIGH)
        GPIO.output(dir2Pin[RIGHT], GPIO.LOW)
        PWM.set_duty_cycle(pwmPin[RIGHT], 50)
        PWM.set_duty_cycle(pwmPin[LEFT], 0)
    else:
        GPIO.output(dir1Pin[LEFT], GPIO.HIGH)
        GPIO.output(dir2Pin[LEFT], GPIO.LOW)
        PWM.set_duty_cycle(pwmPin[LEFT], 70)
        GPIO.output(dir1Pin[RIGHT], GPIO.HIGH)
        GPIO.output(dir2Pin[RIGHT], GPIO.LOW)
        PWM.set_duty_cycle(pwmPin[RIGHT], 70)
    #time.sleep(2)

PWM.stop(pwmPin[LEFT])
PWM.stop(pwmPin[RIGHT])
PWM.cleanup()

GPIO.cleanup()