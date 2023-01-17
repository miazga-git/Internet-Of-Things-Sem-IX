import pandas as pd

import paho.mqtt.client as mqtt
import time


localhost = '127.0.0.1'
port = 1883

topic_0 = "/sensors/temperature"
topic_1 = "/sensors/pressure"
topic_2 = "/sensors/humidity"

table = []
dataframe = pd.read_csv("Table21.csv")

def on_connect(client, userdata, flags, rc):
    print("Connected with result code: " + str(rc))

def on_message(client, userdata, msg):
    global m_decode
    topic = msg.topic
    m_decode = str(msg.payload.decode("utf-8","ignore"))
    time.sleep(1)
    if msg.topic == "/sensors/temperature":
        print("temperature: " + m_decode)
        table.append([msg.payload, time.time()])
        dataframe = pd.DataFrame(table)
        dataframe.to_csv('Table21.csv', index=False)
    elif msg.topic == "/sensors/pressure":
        print("pressure " + m_decode)
    elif msg.topic == "/sensors/humidity":
        print("humidity: " + m_decode)


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(localhost,port)
client.subscribe([(topic_0, 0), (topic_1,1), (topic_2,2)])
client.loop_forever()










