#!/usr/bin/python3

#========================#
#     Import Package     #
#========================#

import paho.mqtt.client as mqtt # If => ImportError: No module named 'paho'
                                # Download paho-mqtt Package
                                # $ pip3 install paho-mqtt
import RPi.GPIO as GPIO
import time

#========================#
#    Setup Parameter     #
#========================#

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17, GPIO.OUT)

MQTT_SERVER = "nta2.shu.edu.tw"
MQTT_PORT   = 1883
MQTT_ALIVE  = 60

#========================#
#    Connect Function    #
#========================#

def on_connect(client, userdata, flags, rc):
    print("MQTT Connected")
    client.subscribe('chuck/led',2)

#========================#
#   Get Data Function    #
#========================#

def on_message(client, userdata, msg):
    payload = msg.payload.decode("utf-8")
    print("MQTT Payload = " ,payload)
    if (payload == '1'):
      GPIO.output(17, True)
    else:
      GPIO.output(17, False)

#========================#
#     Start Connect      #
#========================#

if __name__ == '__main__':
    mqtt_client = mqtt.Client()
    mqtt_client.on_connect = on_connect     #attach function to callback
    mqtt_client.on_message = on_message

    mqtt_client.connect(MQTT_SERVER, MQTT_PORT, MQTT_ALIVE)  #connect to broker
    mqtt_client.loop_forever()              #subscribe forever until ctl+c

GPIO.cleanup()
