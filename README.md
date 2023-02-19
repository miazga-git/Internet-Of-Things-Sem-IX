# Review of Labs 

## FastApi + MQTT

<b>Tasks:</b> 
![image](https://user-images.githubusercontent.com/82395921/212981155-a09254c7-c3b2-467c-891e-cde548c468e7.png)

<b>[English below]</b><br>
Implement communication using the MQTT protocol, the Raspberry PI device should be both a client and a broker
- At least 3 topics and different QoS
- At least 2 subscriptions and 1 publication from paho-mqtt

Implement the REST API service using fast-api and communicate with the API from the level of the client application
  At least 3 services that download data and at least 2 that add/modify data - data stored in the file
  
## SenseHat

<b>Tasks:</b> 

![image](https://user-images.githubusercontent.com/82395921/212981196-380307cc-7e68-4e20-8880-21410bff2576.png)

<b>[English below]</b><br>
Build an application that allows you to use Raspberry PI sensors and actuators
Sensors (at least 4): Accelerometer, Gyroscope, Magnetometer/compass, Thermometer, Humidity sensor, Barometer, Joystick
Actuators: LED display

## Docker Project

<b>Tasks:</b> 
 
![image](https://user-images.githubusercontent.com/82395921/212981060-102af3cc-43d1-4ad8-a780-a6c507cd050d.png)

<b>[English below]</b><br>
4 containers (based on Dockerfile and docker-compose.yml):
- Container with the MQTT broker
- Container with FastAPI services, services also available from the host
- Container with an application that retrieves data from FastAPI after receiving a certain message (MQTT), the data is then published on another topic
- Container with an MQTT client subscribing to a topic that another client is posting about
## AWS + Linear Regression

<b>Tasks:</b> 

![image](https://user-images.githubusercontent.com/82395921/212981234-bdfc055f-139b-4dc3-8012-4717943eb875.png)

<b>[English below]</b><br>
Cloud:
- Defining the activity in the stream (pipeline):
- Determining the value of a new attribute based on others
- Filtering/add other attributes

Locally:
- Define an MQTT client that saves data to a csv file
- Write a script that generates a plot of values against time
- Determine the mean value, standard deviation
- Use at least one ML method

## Useful commands:
```console
 pip install uvicorn
 
 pip3 install fastapi
 
 /home/pi/.local/bin/uvicorn script:app --reload
 
 pip install paho-mqtt
 
 apt-get install mosquitto
 
 apt-get install mosquitto-client
 
 ps -ef | grep mosquitto
```
