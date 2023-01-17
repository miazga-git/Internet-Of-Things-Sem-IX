import os
import paho.mqtt.client as mqtt
import time
import requests

mqtt_host = os.environ['MQTT_HOST']
mqtt_port = int(os.environ['MQTT_PORT'])
api_host = os.environ['API_HOST']
api_port = os.environ['API_PORT']


topic_init = "/init"
topic_after_init = "/after_init"
def on_connect(client, userdata, flags, rc):
    print("Connected with result code: " +str(rc))

def on_message(client,userdata,msg):
    global m_decode
    topic = msg.topic
    m_decode = str(msg.payload.decode("utf-8","ignore"))
    time.sleep(1)
    if msg.topic == "/init":
        print("Message with topic init received")
        response = requests.get("http://"+api_host+":" + api_port + "/records").content
        print(response)
        client.publish(topic_after_init, payload = response, qos=1)
        if m_decode == 0:
            print('message with 0')

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect('mosquitto', mqtt_port)
client.subscribe(topic_init,qos=1)
client.loop_forever()