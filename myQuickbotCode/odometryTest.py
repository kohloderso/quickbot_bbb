import quickbot_config as config
import Adafruit_BBIO.ADC as ADC
import Adafruit_BBIO.PWM as PWM
import Adafruit_BBIO.GPIO as GPIO

GPIO.setup(config.Ol, GPIO.IN)
GPIO.add_event_detect(config.Ol, GPIO.BOTH) # look for RISING or FALLING

if GPIO.event_detected(config.Ol): # Executed in either case
    print "event left detected!"

while True:
    print "things happening here"
    time.sleep(1)

GPIO.cleanup()