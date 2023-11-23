"""
test using:https://www.hivemq.com/demos/websocket-client/

Connecting to propietary HiveMQ cloud cluster

"""

import network
import time
from machine import Pin,reset
import dht
import ujson
from umqtt.simple import MQTTClient

# MQTT Server Parameters
MQTT_CLIENT_ID = "micropython-weather-demo"
MQTT_BROKER    = "broker.mqttdashboard.com"
MQTT_USER      = ""
MQTT_PASSWORD  = ""
MQTT_TOPIC     = "testing_hive"

#callback 
def sub_cb(topic,msg):
  print((topic,msg))

#connecting to wifi
print("Connecting to WiFi", end="")
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect("COWIFI213509242/0","WiFi-92255108")
while not sta_if.isconnected():
  print(".", end="")
  time.sleep(0.1)
print(" Connected!")
print('direccion IP')
print(sta_if.ifconfig())

print("Connecting to MQTT server... ", end="")
client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER, user=MQTT_USER, password=MQTT_PASSWORD)

###########publishing
# client.connect()
# try:
#     message='connected from ESP8266'
#     print("Reporting to MQTT topic {}: {}".format(MQTT_TOPIC, message))
#     client.publish(MQTT_TOPIC, message)
# except:
#    print("publishing message failed, rebooting system")
#    reset()



######subscription
last_message=time.time()

#setting callback
client.set_callback(sub_cb)

client.connect()
print("Connected!")
try:
    #subscribing to topic
    client.subscribe(MQTT_TOPIC)
    print("successful subscription")
except:
   print('connection failed, reseting system')
   reset()
else:
    while True:
        try:
            client.check_msg()
            if (time.time() - last_message) > 5:
                msg='response to subscription from ESP8266'
                client.publish(MQTT_TOPIC, msg)
                last_message = time.time()
        except OSError:
           
           reset()
        
