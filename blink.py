import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

LED = 23
GPIO.setup(LED, GPIO.OUT)

try:
    while True:
        print("On")
        GPIO.output(LED, GPIO.HIGH)
        time.sleep(1)
        print("Off")
        GPIO.output(LED, GPIO.LOW)
        time.sleep(1)
        
except KeyboardInterrupt:
    print("I'm done!")
finally:
    GPIO.output(LED, GPIO.LOW)
    GPIO.cleanup()