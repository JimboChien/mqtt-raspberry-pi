#!/usr/bin/python3

#========================#
#     Import Package     #
#========================#

import paho.mqtt.client as mqtt # If => ImportError: No module named 'paho'
                                # Download paho-mqtt Package
                                # $ pip3 install paho-mqtt
import RPi.GPIO as GPIO
import time
import Adafruit_DHT             # $ pip3 install Adafruit_DHT

#========================#
#     Setup Parameter    #
#========================#

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17, GPIO.OUT)

MQTT_SERVER = "nta2.shu.edu.tw"
MQTT_PORT   = 1883
MQTT_ALIVE  = 60

#========================#
#    Publish Function    #
#========================#

def Publish_DHT():
    client = mqtt.Client()

    #------------MQTT Publish Connect------------#
    client.connect(MQTT_SERVER, MQTT_PORT, MQTT_ALIVE)

    #-----------MQTT Publish-----------#
    #-------dht-------#
    ts = str(str(time.time()).split(".")[0])
    h, t = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 14)
    if h is not None and t is not None:
        print(f'Temp : {t:3>} °C/{t * 1.8 + 32:3>} °F\nHumidity : {h:3>} %')

        client.connect(MQTT_SERVER, MQTT_PORT, MQTT_ALIVE)
        client.publish('chuck/temp_c', t)
        client.connect(MQTT_SERVER, MQTT_PORT, MQTT_ALIVE)
        client.publish('chuck/temp_f', t * 1.8 + 32)
        client.connect(MQTT_SERVER, MQTT_PORT, MQTT_ALIVE)
        client.publish('chuck/humid', h)

    else:
        print('Failed to get reading. Try again!')

if __name__ == '__main__':
             
    while True:
        Publish_DHT()
        time.sleep(1)


GPIO.cleanup()
