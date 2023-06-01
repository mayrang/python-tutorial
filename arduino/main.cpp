#include <Arduino.h>
#include <ESP8266WiFi.h>
#include <PubSubClient.h>

const char *ssid = "Hanbat_WLAN_Guest";
const char *password = "";
const char *mqtt_server = "broker.emqx.io";

WiFiClient espClient;
PubSubClient client(espClient);

#include "DHT.h"

#define DHTPIN 10     // Digital pin connected to the DHT sensor
#define DHTTYPE DHT22 // DHT 22
DHT dht(DHTPIN, DHTTYPE);

const int ledR = 16;
const int ledG = 5;
const float vref = 3.3;

void callback(char *topic, byte *payload, unsigned int length);
void setupWifi();
void reconnect();
void sendData();


void setup()
{
  Serial.begin(9600);
  Serial.println("Program Start !!");
  setupWifi();
  client.setServer(mqtt_server, 1883);
  client.setCallback(callback);

  // 신호등 핀 설정
  pinMode(ledR, OUTPUT);
  pinMode(ledG, OUTPUT);

  // 꺼짐으로 시작
  digitalWrite(ledR, LOW);
  digitalWrite(ledG, LOW);

  dht.begin();
}

long lastMsg = 0;

void loop()
{
  if (!client.connected())
  {
    reconnect();
  }
  client.loop();

  long now = millis();
  if (now - lastMsg > 5000) {
    sendData();
    lastMsg = now;
  }
}

void sendData() {

  int cdsValue = analogRead(A0);

  float voltage = (1023 - cdsValue) * vref / 1023.0;
  // Serial.println(voltage);
  float lux = 27.565 * pow(10, voltage);
  //  float lux = pow(10, ((log10(voltage) - log10(0.01)) / 0.5));
  // Serial.println(lux);

  float humidity = dht.readHumidity();
  float temperature = dht.readTemperature();

  if (isnan(humidity) || isnan(temperature))
  {
    Serial.println("DHT22 sensor error!");
    // pinMode(DHTPIN, OUTPUT);
    // digitalWrite(DHTPIN, LOW);
    // delay(10);
    // digitalWrite(DHTPIN, HIGH);
    // pinMode(DHTPIN, INPUT);

    return;
  }

  // String sendMessage = "Humidity: " + String(humidity) + "% Temperature: " + String(temperature) + ", Lux: " + String(lux);

  String sendMessage = "{\"humidity\": " + String(humidity) + ",\"temperature\": " + String(temperature) + ",\"lux\": " + String(lux) + "}";

  Serial.println(sendMessage);

  client.publish("mobile/00/sensing", sendMessage.c_str());

}

void setupWifi()
{

  delay(10);
  // We start by connecting to a WiFi network
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);

  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED)
  {
    delay(500);
    Serial.print(".");
  }

  randomSeed(micros());

  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
}

void callback(char *topic, byte *payload, unsigned int length)
{
  Serial.print("Message arrived [");
  Serial.print(topic);
  Serial.print("] ");
  String receivedMessage = "";
  for (unsigned int i = 0; i < length; i++)
  {
    receivedMessage += (char)payload[i];
  }
  Serial.println(receivedMessage);
  receivedMessage.toLowerCase();

  if (receivedMessage.startsWith("on"))
  {
    digitalWrite(ledR, HIGH);
  }
  else if (receivedMessage.startsWith("off"))
  {
    digitalWrite(ledR, LOW);
  }
}

void reconnect()
{
  // Loop until we're reconnected
  while (!client.connected())
  {
    Serial.print("Attempting MQTT connection...");
    // Create a random client ID
    String clientId = "Mobile-";
    clientId += String(random(0xffff), HEX);
    // Attempt to connect
    if (client.connect(clientId.c_str()))
    {
      Serial.println("connected");
      client.subscribe("mobile/00/led");
    }
    else
    {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      // Wait 5 seconds before retrying
      delay(5000);
    }
  }
}
