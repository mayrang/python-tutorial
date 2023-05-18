import paho.mqtt.client as mqtt
import json
import time

def on_message(client, userdata, message):
    result = str(message.payload.decode("utf-8"))
    sensing = json.loads(result)
    print(f"temperarue = {sensing['temperature']}\nhumidity = {sensing['humidity']}")

MQTT_SUB_TOPIC = 'mobile/mayrang/sensing'
MQTT_HOST = "broker.emqx.io"
MQTT_PORT= 1883
MQTT_KEEPALIVE_INTERVAL = 60

client = mqtt.Client()
client.on_message = on_message

client.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL)
client.subscribe(MQTT_SUB_TOPIC)
client.loop_start()

try:
    while True:
        time.sleep(5)
        print("waiting..")
except KeyboardInterrupt:
    print("I'm done")
finally:
    client.disconnect()