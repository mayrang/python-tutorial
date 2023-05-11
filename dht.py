import time
import adafruit_dht
import psutil


for proc in psutil.process_iter():
    if proc.name() == "libgpiod_pulsein":
        proc.kill()

dht_device = adafruit_dht.DHT22(4)

try:
    while True:
        try:
            temperature = dht_device.temperature
            humidity = dht_device.humidity
            print(f"Temperature = {temperature:0.1f}*C Humidity = {humidity:0.1f}%")
        except RuntimeError:
            time.sleep(1.0)
        time.sleep(2.0)
except KeyboardInterrupt:
    print("사용자가 프로그램을 종료했습니다.")
finally:
    dht_device.exit()
