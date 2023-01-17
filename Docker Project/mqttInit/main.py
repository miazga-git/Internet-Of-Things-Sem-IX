import os
import paho.mqtt.client as mqtt
import requests

mqtt_host = os.environ['MQTT_HOST']
mqtt_port = int(os.environ['MQTT_PORT'])
api_host = os.environ['API_HOST']
api_port = os.environ['API_PORT']


topic_init = "/init"
def on_connect(client, userdata, flags, rc):
    print("Connected with result code: " +str(rc))

def publish(client):
    response = "inicjacja"
    client.publish(topic_init, payload = response, qos=1)

client = mqtt.Client()
client.on_connect = on_connect

client.connect('mosquitto', mqtt_port)
publish(client)
client.disconnect()