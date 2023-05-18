import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
time_stamp = time.time()

def my_callback(channel):
    global time_stamp       # put in to debounce  
    time_now = time.time()  
    if (time_now - time_stamp) >= 0.3:  
        print("You pressed the button")
    time_stamp = time_now 

BUTTON = 24
GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(BUTTON, GPIO.RISING, callback=my_callback)

try:
    i = 0
    while (True):
        time.sleep(1)
        i = i + 1
        print(i)

except KeyboardInterrupt:
    print("I'm done!")
    GPIO.cleanup()
