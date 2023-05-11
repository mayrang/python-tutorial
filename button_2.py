import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
time_stamp = time.time()
def my_callback(channel):
    global time_stamp
    time_now = time.time()
    if(time_now - time_stamp) >= 0.3:
        print("You pressed the button")
    time_stamp = time_now

BUTTON = 24
GPIO.setup(BUTTON, GPIO.IN,
pull_up_down=GPIO.PUD_DOWN)
# 인터럽트 (INTERRUPT)
GPIO.add_event_detect(BUTTON, GPIO.RISING, callback=my_callback)


try:
    num = 1
    while True:
        print(num)
        time.sleep(1)
        num += 1
except KeyboardInterrupt:
    print("I'm Done")
finally:
    GPIO.cleanup()
