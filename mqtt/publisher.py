import paho.mqtt.client as mqtt
import json
import time


MQTT_PUB_TOPIC = 'mobile/mayrang/sensing'
MQTT_HOST = "broker.emqx.io"
MQTT_PORT= 1883
MQTT_KEEPALIVE_INTERVAL = 60

client = mqtt.Client()

client.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL)

client.loop_start()

try:
    while True:
        time.sleep(10)
        humidity, temperature = 80, 30
        sensing = {
            "humidity": humidity,
            "temperature": temperature
        }
        value = json.dumps(sensing)
        client.publish(MQTT_PUB_TOPIC, value)
        print(value)
except KeyboardInterrupt:
    print("I'm done")
finally:
    client.disconnect()