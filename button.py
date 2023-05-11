import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

BUTTON = 24
GPIO.setup(BUTTON, GPIO.IN,
pull_up_down=GPIO.PUD_DOWN)

try:
    num = 1
    while True:
        if GPIO.input(BUTTON) == True:
            print(f"You pressed the button{num}")
            num += 1
        time.sleep(0.1)
except KeyboardInterrupt:
    print("I'm Done")
finally:
    GPIO.cleanup()