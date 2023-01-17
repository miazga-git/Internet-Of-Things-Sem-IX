import time
import paho.mqtt.client as mqtt
from random import randrange

localhost = '127.0.0.1'
port = 1883

topic_0 = "/sensors/temperature"
topic_1 = "/sensors/blood_pressure"
topic_2 = "/parameters/time_of_sleep"


def on_connect(client, userdata, flags, rc):
    print("Connected with result code: " + str(rc))

def publish(client):
    qos = 0
    while True:
        time.sleep(2)

        if qos == 3:
            qos = 0

        if qos == 0:
            result = client.publish(topic_0, randrange(100), qos)
            print("Temperature info sent")
        elif qos == 1:
            result = client.publish(topic_1, randrange(1000), qos)
            print("Pressure info sent")
        elif qos == 2:
            result = client.publish(topic_2, randrange(100), qos)
            print("Time of sleep info sent")

        status = result[0]

        if status == 0:
            print("Message sent, qos = " + str(qos))
            qos = qos +1
        else:
            print("Massage sending failure")



client = mqtt.Client()
client.on_connect = on_connect
client.connect(localhost,port)
publish(client)

client.disconnect()





